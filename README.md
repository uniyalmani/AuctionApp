# AuctionApp
Biding for diffrent auction 
admin email and password for geting token for creating auction
```
{
adminemail-> nitinuniyal21@gmail.com
password -> 9410197255
}
```

# admin routes 
* **admin login**
* method --> **post** --> **/login/admin**
request body 
```
{
    email: str
    password:str
}
```
* **create auction** 
** header token reuired for autherization**
* method --> **post ->**  **/create_auction**
request body 
```
{
    title: str
    start_time: datetime # utc 
    end_time: datetime  #utc
    start_amount: float
    discription: str

}
```

---------------------------
# common user routes 

* **common user sign up**
* method -> **post ->**  **/signup**
requestbody - > 
```
{
    name:str
    email: str
    password:str
}
```
* **common user login**
* method -> **post -->**  **/login/user**
requsestbody ->
```
{
    email: str
    password:str
}
```
* common method for geting all bids for an auction **no autherization required**
* method **get -->**  **/auction_offered_bids/{auction_id}**

* common method **no authentication reuired **
* **list all auction **
* method **get -->** **/all_auction**


* user method offer bit **header token required for autherization**
* method -> **post -> ** **/offer_bid**
```
{
    offered_amount: float
    auction_id: int
   }
```



