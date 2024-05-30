from src.apis.DB.db_connection import *

def create_database_users():
    try:
        db = db_connect()
        # Defining the SQL query to check if the database exists
        check_db_query = "SHOW DATABASES LIKE 'demo'"

        # Executing the SQL query to check if the database exists
        result = db.execute_query(check_db_query)

        if result:
            print("Database already exists.")
            return

        # Defining the SQL query to create the database if it doesn't exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS demo"

        # Executing the SQL query to create the database
        db.execute_query(create_db_query)
        db.commit()
        db.close()
        print("Database created successfully.")

    except Exception as err:
        print(f"An error occurred: {err}")

def create_user_table():
    try:
        db = db_connect()
        # Defining SQL query to check if the users table already exists
        check_table_query = "SHOW TABLES LIKE 'inventory_item'"

        # Executing the SQL query to check if the table exists
        result = db.execute_query(check_table_query)

        # create table if it doesn't exist
        if not result:
            create_table_query = """
            CREATE TABLE inventory_item (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL UNIQUE,
                category VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                quantity INT NOT NULL,
                description VARCHAR(500),
                currency VARCHAR(10) DEFAULT 'INR',
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            """

            # Executing the SQL query to create the users table
            db.execute_query(create_table_query)

            # Commit the transaction
            db.commit()
            db.close()
            print("Table 'inventory_item' created successfully.")
        else:
            print("Table 'inventory_item' already exists.")

    except Exception as err:
        print(f"An error occurred while creating the table: {err}")


create_database_users()
create_user_table()
def get_db_connection():
    return db_connect()
