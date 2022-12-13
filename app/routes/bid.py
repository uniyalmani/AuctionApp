from pydantic import BaseModel, validator
from typing import Union
from fastapi import APIRouter, Depends,Header
# from app.utilities.dependencies import get_session
from app.utilities.helpers import hash_password, verify_password, create_jwt_token, is_valid_token
from app.utilities.dependencies import get_decoded_token_data
from app.services import bidserver
from datetime import datetime

router = APIRouter()

print("helllolkdlslfl")
class AuctionModel(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime
    start_amount: float
    discription: str

@router.post('/create_auction',
        tags=["Admin Routes"],
        description="**Route for creating auction**")
def create_auction(auction_info: AuctionModel, 
    auction: object = Depends(bidserver.AuctionOperatorAdmin),
    token: Union[str, None] = Header(default=None)):
    
    data = get_decoded_token_data(token)
    if not data["valid_token"] or data["role"] != "admin":
        return {
            "data":[],
            "error":"invalid token please try to login as admin",
            "message": "failed to create auction"
        }
    auction_info = dict(auction_info)
    data =auction.create_new_auction(auction_info)
    
    return data



@router.get('/auction_offered_bids/{auction_id}',
        tags=["Common Routes"],
        description="**Route for offering bid**")
def auction_offered_bids(auction_id: int, 
    auction: object = Depends(bidserver.Userbids)):
    
    data = auction.get_bid_offered_by_auction_id(auction_id)
   
    
    return data


@router.get('/all_auction',
        tags=["Common Routes"],
        description="**Route for creating account**")
def auction_offered_bids( 
    auction: object = Depends(bidserver.Userbids)):
    
    data = auction.list_all_auction()
    return data



class OfferBid(BaseModel):
    offered_amount: float
    auction_id: int


@router.post('/offer_bid',
        tags=["user Routes"],
        description="**Route for offering bid**")
def offer_bid(offer_bid_info: OfferBid, 
    auction: object = Depends(bidserver.Userbids),
    token: Union[str, None] = Header(default=None)):
    
    data = get_decoded_token_data(token)
    if not data["valid_token"] :
        return {
            "data":[],
            "error":"invalid token please try to login as user",
            "message": "failed to make bit"
        }

    offer_bid_info = dict(offer_bid_info)

    offer_bid_info["user_email"] = data["email"]
    offer_bid_info = dict(offer_bid_info)
    data = auction.offer_bid(offer_bid_info)

    
    return data