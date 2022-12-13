# AuctionApp
* Biding for diffrent auction for running app on local use git clone for cloning this repo on your local 
* run command docker-compose up
* * for swagger documentation use ** /docs ** route 

* **admin email and password for geting token for creating auction **
```
{
adminemail-> nitinuniyal21@gmail.com
password -> 9410197255
}
```

# admin routes 
***1)** **admin login**
* method --> **post** --> **/login/admin**
request body 
```
{
    email: str
    password:str
}
```
***2)** **create auction** 
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

* **1)**  **common user sign up**
* method -> **post ->**  **/signup**
requestbody - > 
```
{
    name:str
    email: str
    password:str
}
```
* **2)** **common user login**
* method -> **post -->**  **/login/user**
requsestbody ->
```
{
    email: str
    password:str
}
```
* **3)** common method for geting all bids for an auction **no autherization required**
* method **get -->**  **/auction_offered_bids/{auction_id}**

* *4)**common method **no authentication reuired **
* **list all auction **
* method **get -->** **/all_auction**


* **5)** user method offer bit **header token required for autherization**
* method -> **post -> ** **/offer_bid**
```
{
    offered_amount: float
    auction_id: int
   }
```



