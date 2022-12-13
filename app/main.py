from fastapi import FastAPI
# from app.models import database_models
from app.migration import Migratetion
from app.controllers.database_initializer import init_db
from app.routes import auth, bid
import os

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.on_event("startup")
def on_startup():
    print("start")
    init_db()
    print("end")
    migrate = Migratetion()
    migrate.create_role("admin")
    migrate.create_role("user")
    env = os.environ
    user_data = {"name": env.get("NAME"), 
                "email":env.get("EMAIL"),
                "password": env.get("PASSWORD")}
    migrate.create_admin(user_data)


app.include_router(auth.router)
app.include_router(bid.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}

