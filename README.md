
# Internet Order Management Application

This Python application allows users to manage and monitor internet orders using a simple RESTful API. It provides endpoints for creating, retrieving, updating, and deleting orders.

## Features
- Create new orders with customer details, items, and quantity.
- Retrieve all existing orders.
- Update order details or statuses.
- Delete orders.

## Technologies Used
- **Python**: Core programming language.
- **Flask**: Web framework for creating RESTful APIs.
- **SQLite**: Lightweight database for storing order data.

## API Endpoints
### 1. Get All Orders
**GET** `/orders`  
Response:
```json
[
    {
        "id": 1,
        "customer_name": "John Doe",
        "item": "Laptop",
        "quantity": 1,
        "status": "Pending"
    }
]
```

### 2. Create an Order
**POST** `/orders`  
Request Body:
```json
{
    "customer_name": "John Doe",
    "item": "Laptop",
    "quantity": 1
}
```
Response:
```json
{
    "message": "Order created successfully"
}
```

### 3. Update an Order
**PUT** `/orders/<order_id>`  
Request Body:
```json
{
    "customer_name": "Jane Doe",
    "item": "Smartphone",
    "quantity": 2,
    "status": "Shipped"
}
```
Response:
```json
{
    "message": "Order updated successfully"
}
```

### 4. Delete an Order
**DELETE** `/orders/<order_id>`  
Response:
```json
{
    "message": "Order deleted successfully"
}
```

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required dependencies:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Use tools like Postman or cURL to interact with the API.

## License
This project is licensed under the MIT License.
