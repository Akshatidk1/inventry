from fastapi import APIRouter
from src.apis.inventory.inventory_schema import IventryRegistration
from src.apis.DB.db_connection import *
from src.apis.inventory.inventory import *

router = APIRouter()

# router for registering the item
@router.post("/addItem",tags=['Inventory'])
async def register_endpoint(user: IventryRegistration):
    db = db_connect()
    return await AddInventory(user,db)

@router.post("/getAllItems",tags=['Inventory'])
async def get_all():
    try:
        data = get_all_product()
        return data
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        return {"error": True, 'message': f'Error: {str(e)}'}


@router.post("/updateItem",tags=['Inventory'])
async def updade_endpoint(item_id: int, item: IventryRegistration):
    db = db_connect()
    return await UpdateInventory(item_id,item,db)

@router.post("/deleteItem",tags=['Inventory'])
async def delete_endpoint(item_id: int):
    db = db_connect()
    return await DeleteInventory(item_id,db)