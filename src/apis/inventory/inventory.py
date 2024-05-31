from fastapi import HTTPException, status
from src.apis.inventory.inventory_schema import IventryRegistration # import the InventoryRegistration schema
from src.apis.DB.db_connection import * # import the database connection
import pandas as pd

# Logic for registering the items
async def AddInventory(item: IventryRegistration, db):
    """
    Add an inventory item from the database.

    :param item: The info of the inventory item to add.
    :param db: The database connection.
    :return: A dictionary containing a success message and the item ID.
    """
    try:
        # Check if required fields are provided
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

        # Check if item already exists
        existing_user = db.execute_query("SELECT * FROM inventory_item WHERE name = %s", (item.name,))
        if existing_user:
            raise HTTPException(status_code=400, detail="Item already exists")

        # Insert the item into the database
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
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Function to get all products
def get_all_product():
    """
    Get All Product.
    :return: A dictionary containing all product available.
    """
    try:
        db = db_connect()
        query = """SELECT id,name,category,price,description,quantity FROM inventory_item"""
        df = db.fetch_df(query)
        data = df.to_dict(orient='records')
        return {'error':False,'data':data}
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        return {"error": True, 'message': f'Error: {str(e)}'}

# Logic for updating the items
async def UpdateInventory(item_id: int, item: IventryRegistration, db):
    """
    Update an inventory item from the database.

    :param item_id: The ID of the inventory item to update.
    :param item: The info of the inventory item to update.
    :param db: The database connection.
    :return: A dictionary containing a success message and the item ID.
    """
    try:
        # Check if required fields are provided
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

        # Check if item exists
        existing_item = db.execute_query("SELECT * FROM inventory_item WHERE id = %s", (item_id,))
        if not existing_item:
            raise HTTPException(status_code=404, detail="Item not found")

        # Update the item in the database
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
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
# Logic for deleting the items
async def delete_inventory(item_id: int, db):
    """
    Delete an inventory item from the database.

    :param item_id: The ID of the inventory item to delete.
    :param db: The database connection.
    :return: A dictionary containing a success message and the item ID.
    """
    try:
        # Check if item exists
        existing_item = db.execute_query("SELECT * FROM inventory_item WHERE id = %s", (item_id,))
        if not existing_item:
            raise HTTPException(status_code=404, detail="Item not found")

        # Delete the item from the database
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
        # Log the error and raise an internal server error
        print(f"Error on line {sys.exc_info()[-1].tb_lineno}: {type(e).__name__}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Function to get a product by ID
def get_product_by_id(item_id: int):
    """
    Get an inventory item by ID from the database.

    :param item_id: The ID of the inventory item to retrieve.
    :return: A dictionary containing the item details or an error message.
    """
    try:
        db = db_connect()
        query = f"""SELECT id,name,category,price,description,quantity FROM inventory_item where id = {item_id}"""
        df = db.fetch_df(query)
        data = df.to_dict(orient='records')
        return {'error':False,'data':data}
    except Exception as e:
        # Log the error and return an error message
        print(f"Error on line {sys.exc_info()[-1].tb_lineno}: {type(e).__name__}: {e}")
        return {"error": True, 'message': f'Error: {str(e)}'}