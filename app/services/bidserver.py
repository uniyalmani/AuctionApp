import os
from datetime import datetime
from fastapi import FastAPI, Response, status
from typing import Dict, List, Optional
from sqlmodel import Field, SQLModel, select
from sqlalchemy import UniqueConstraint, String, desc
from sqlalchemy import Column
from app.utilities.helpers import hash_password, verify_password, create_jwt_token
from app.utilities.dependencies import get_session
from app.models.database_models import Role, User, Auction, UserBid




class AuctionOperatorAdmin:
    def __init__(self):
        self.session = next(get_session())


    def create_new_auction(self, auction_info):
        try:
            auction =  Auction(
                        title=auction_info["title"],
                        start_time=auction_info["start_time"],
                        end_time=auction_info["end_time"],
                        start_amount=auction_info["start_amount"],
                        discription=auction_info["discription"]
                    )

            if auction_info["start_time"] > auction_info["end_time"]:
                return {
                "error": "start time should be less then end time",
                "data": [
                    {
                        "auction": {}
                        }
                ],
                "message":"failed to create auction change title"
            }

            self.session.add(auction)
            self.session.flush()
            self.session.commit()
            return {
                "error": None,
                "data": [
                    {
                        "auction": auction_info
                        }
                ],
                "message":"auction suceesfully created "
            }
        except Exception as e:
            return {
                "error": e,
                "data": [
                    {
                        "auction": {}
                        }
                ],
                "message":"failed to create auction change title"
            }
        
        


class Userbids:
    def __init__(self):
        self.session = next(get_session())


    def offer_bid(self, offer_bid_info):
        query = select(Auction).where(Auction.id == offer_bid_info["auction_id"])
        auction_info = self.session.exec(query).first()
       
    
        if not auction_info:
            return {
                "error" : "no auction exist",
                "data" : [],
                "message": "Auction is already soled"
            }

        auction_info = dict(auction_info)
        current_time = datetime.utcnow()

        if auction_info["end_time"] < current_time:
            return {
                "error" : "expired bid",
                "data" : [],
                "message": "Auction is already soled"
            }

        if auction_info["current_top_bid"] > offer_bid_info["offered_amount"] :
            curr_bid_amount = auction_info["current_top_bid"]
            message = f"biding amount should be higher then {curr_bid_amount}"
            return {
                "error" : "low biding ammount",
                "data" : [],
                "message": message
            }

        if auction_info["start_amount"] > offer_bid_info["offered_amount"] :
            curr_bid_amount = auction_info["start_amount"]
            message = f"biding amount should be higher then {curr_bid_amount}"
            return {
                "error" : "low biding ammount",
                "data" : [],
                "message": message
            }

        user_bid =  UserBid(
                auction_id=offer_bid_info["auction_id"],
                user_email=offer_bid_info["user_email"],
                bid_amount =offer_bid_info["offered_amount"],
            )
        statement = select(Auction).where(Auction.id == auction_info["id"])
        results = self.session.exec(statement)
        auction = results.one()
        auction.current_top_bid = offer_bid_info["offered_amount"]
        self.session.add(auction)
        self.session.add(user_bid)
        self.session.flush()
        self.session.commit()

        return {
                "error" : None,
                "data" : [{"auction_info":auction_info,
                     "offer_bid_info" :offer_bid_info  
                }],
                "message": "bid succesfully"
            }


    def list_all_auction(self):
        query = select(Auction)
        result = self.session.exec(query).all()
        return {
                "error":None,
                "data": [
                    {
                        "auction_info":result,
                    }
                ],
                "message": "sucessfull"
                            }

    def get_bid_offered_by_auction_id(self, id):
        try:
            query = select(Auction).where(Auction.id == id)
            auction_info = self.session.exec(query).first()

            query = select(UserBid).where(UserBid.auction_id == id).order_by(desc(UserBid.bid_amount))
            result = self.session.exec(query).all()
            
            return {
                "error":None,
                "data": [
                    {
                        "auction_info":auction_info,
                        "bids_offered":result
                    }
                ],
                "message": "sucessfull"
                            }


        except Exception as e:
            return {
                "error": e,
                "data": [],
                "message": "failed"
            }

    