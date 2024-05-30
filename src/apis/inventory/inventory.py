from fastapi import HTTPException, status
from src.apis.inventory.inventory_schema import IventryRegistration
# from src.apis.DB.database import get_db_connection

# Logic for registering the user
async def AddInventory(item: IventryRegistration, db):
    try:
        print(db)
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
            "user": item.name,
            "status": status.HTTP_201_CREATED,
        }

    except HTTPException as http_error:
        raise http_error  
    except Exception as e:
        print("error ", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")