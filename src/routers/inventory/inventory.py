from fastapi import APIRouter
from src.apis.inventory.inventory_schema import IventryRegistration
from src.apis.DB.db_connection import *
from src.apis.inventory.inventory import *

router = APIRouter()

# router for registering the item
@router.post("/addItem",tags=['Inventory'])
async def register_endpoint(user: IventryRegistration):
    # Connect to the database
    db = db_connect()
    # Call the AddInventory function to add the item to the inventory
    return await AddInventory(user,db)

@router.post("/getAllItems",tags=['Inventory'])
async def get_all():
    try:
        # Call the get_all_product function to retrieve all items in the inventory
        data = get_all_product()
        return data
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        return {"error": True, 'message': f'Error: {str(e)}'}

@router.post("/updateItem",tags=['Inventory'])
async def updade_endpoint(item_id: int, item: IventryRegistration):
    # Connect to the database
    db = db_connect()
    # Call the UpdateInventory function to update the item in the inventory
    return await UpdateInventory(item_id,item,db)

@router.post("/deleteItem",tags=['Inventory'])
async def delete_endpoint(item_id: int):
    # Connect to the database
    db = db_connect()
    # Call the DeleteInventory function to delete the item from the inventory
    return await DeleteInventory(item_id,db)

@router.post("/getItem",tags=['Inventory'])
async def get_product(item_id: int):
    try:
        # Call the get_product_by_id function to retrieve the item from the inventory
        data = get_product_by_id(item_id)
        return data
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        return {"error": True, 'message': f'Error: {str(e)}'}