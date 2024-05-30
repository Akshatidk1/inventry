from fastapi import HTTPException, status
from src.apis.inventory.inventory_schema import IventryRegistration
from src.apis.DB.db_connection import *
import pandas as pd


# Logic for registering the items
async def AddInventory(item: IventryRegistration, db):
    try:
        print(item)
        if not item.name:
            raise HTTPException(status_code=400, detail="Name is required")

        if not item.category:
            raise HTTPException(
                status_code=400, detail="Category not provided"
            )

        if not item.price:
            raise HTTPException(
                status_code=400, detail="Price not provided"
            )
        if not item.currency:
            raise HTTPException(
                status_code=400, detail="Currency not provided"
            )

        
        existing_user = db.execute_query("SELECT * FROM inventory_item WHERE name = %s", (item.name,))
        if existing_user:
            raise HTTPException(status_code=400, detail="Item already exists")

        sql = "INSERT INTO inventory_item (name, category, price, quantity, description, currency) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (item.name, item.category, item.price, item.quantity, item.description, item.currency)
        db.execute_query(sql, val)
        db.commit()
        db.close()
        return {
            "message": "Item Added successfully",
            "item": item.name,
            "status": status.HTTP_201_CREATED,
        }

    except HTTPException as http_error:
        raise http_error  
    except Exception as e:
        print("error ", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

def get_all_product():
    try:
        db = db_connect()
        query = """SELECT id,name,category,price,description,quantity FROM inventory_item"""
        df = db.fetch_df(query)
        data = df.to_dict(orient='records')
        return {'error':False,'data':data}
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        return {"error": True, 'message': f'Error: {str(e)}'}
    

async def UpdateInventory(item_id: int, item: IventryRegistration, db):
    try:
        if not item.name:
            raise HTTPException(status_code=400, detail="Name is required")

        if not item.category:
            raise HTTPException(
                status_code=400, detail="Category not provided"
            )

        if not item.price:
            raise HTTPException(
                status_code=400, detail="Price not provided"
            )
        if not item.currency:
            raise HTTPException(
                status_code=400, detail="Currency not provided"
            )

        existing_item = db.execute_query("SELECT * FROM inventory_item WHERE id = %s", (item_id,))
        if not existing_item:
            raise HTTPException(status_code=404, detail="Item not found")

        sql = """
            UPDATE inventory_item 
            SET name = %s, category = %s, price = %s, quantity = %s, description = %s, currency = %s 
            WHERE id = %s
        """
        val = (item.name, item.category, item.price, item.quantity, item.description, item.currency, item_id)
        db.execute_query(sql, val)
        db.commit()
        db.close()
        return {
            "message": "Item Updated successfully",
            "item_id": item_id,
            "status": status.HTTP_200_OK,
        }

    except HTTPException as http_error:
        raise http_error  
    except Exception as e:
        print("error ", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def DeleteInventory(item_id: int, db):
    try:
        existing_item = db.execute_query("SELECT * FROM inventory_item WHERE id = %s", (item_id,))
        if not existing_item:
            raise HTTPException(status_code=404, detail="Item not found")

        sql = "DELETE FROM inventory_item WHERE id = %s"
        db.execute_query(sql, (item_id,))
        db.commit()
        db.close()
        return {
            "message": "Item Deleted successfully",
            "item_id": item_id,
            "status": status.HTTP_200_OK,
        }

    except HTTPException as http_error:
        raise http_error  
    except Exception as e:
        print("error ", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
