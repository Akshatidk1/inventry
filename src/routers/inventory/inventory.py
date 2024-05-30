from fastapi import APIRouter
from src.apis.inventory.inventory_schema import IventryRegistration
from src.apis.DB.db_connection import *
from src.apis.inventory.inventory import *

router = APIRouter()

# router for registering the item
@router.post("/register")
async def register_endpoint(user: IventryRegistration):
    db = db_connect()
    return await AddInventory(user,db)

