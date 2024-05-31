# Product Inventory Management API

This repository contains a production-ready and dockerized FastAPI application for managing a product inventory. The application provides CRUD APIs for creating, retrieving, updating, and deleting products.

## Features

- **Framework**: FastAPI
- **CRUD APIs for managing products**:
  - Get a single product by ID
  - Get all products
  - Update a product by ID
  - Delete a product by ID
- **Product model** with the following attributes:
  - `id`: Integer (Primary Key)
  - `name`: String
  - `category`: String
  - `price`: Float
- **Database integration**
- **Dockerized for production**
- **Type hints and ORM usage**
- **Adherence to REST API design best practices**

## Requirements

- Python 3.11+
- Docker

## Project Structure

C:.
├── .gitignore
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
└── src
├── apis
│ ├── DB
│ │ ├── database.py
│ │ ├── db_connection.py
│ │ └── MySqlWrapper.py
│ └── inventory
│ ├── inventory.py
│ └── inventory_schema.py
└── routers
└── inventory
└── inventory.py


## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Akshatidk1/inventry.git
    cd inventry
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Update database connection details**:

    Modify the database connection details in `src/apis/DB/db_connection.py` to match your database configuration.


## Running the Application

1. **Run the FastAPI application**:

    ```bash
    uvicorn main:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

## Docker Setup

1. **Build the Docker image**:

    ```bash
    docker build -t product-inventory-api .
    ```

2. **Run the Docker container**:

    ```bash
    docker run -d -p 8000:8000 product-inventory-api
    ```

    The API will be available at `http://127.0.0.1:8000`.

    The FastAPI Swagger UI be available at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Add an Item

- **URL**: `/addItem`
- **Method**: `POST`
- **Body**: JSON representation of the item to be added
- **Response**: JSON representation of the added item

### Get All Items

- **URL**: `/getAllItems`
- **Method**: `POST`
- **Response**: JSON array of all items

### Update an Item by ID

- **URL**: `/updateItem`
- **Method**: `POST`
- **Body**: JSON representation of the item to be updated and its ID
- **Response**: JSON representation of the updated item

### Delete an Item by ID

- **URL**: `/deleteItem`
- **Method**: `POST`
- **Body**: JSON representation of the item ID to be deleted
- **Response**: Success message

### Get a Single Item by ID

- **URL**: `/getItem`
- **Method**: `POST`
- **Body**: JSON representation of the item ID to be retrieved
- **Response**: JSON representation of the item

## Models

### Product

- `id` (INT AUTO_INCREMENT PRIMARY KEY)
- `name` (VARCHAR(255) NOT NULL UNIQUE)
- `category` (VARCHAR(255) NOT NULL)
- `price` (DECIMAL(10, 2) NOT NULL)
- `quantity` (INT NOT NULL)
- `description` (VARCHAR(500))
- `currency` (VARCHAR(10) DEFAULT 'INR')
- `created_at` (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)

```sql
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

## Author

- [Akshat Kumar Nishad](https://github.com/Akshatidk1)

## Submission Details

- [GitHub Repository Link](https://github.com/Akshatidk1/inventry.git)