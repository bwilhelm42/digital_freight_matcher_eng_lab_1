from fastapi import FastAPI

from api.db_routes import router as data_router
from api.price import router as price_router
from api.routes import router as routes_router
from db.database import create_tables

app = FastAPI()

app.include_router(data_router)
app.include_router(price_router)
app.include_router(routes_router)


@app.on_event("startup")
def on_startup():
    create_tables()


@app.get("/")
def read_root():
    return "Welcome to the Digital Freight Matcher API!"
