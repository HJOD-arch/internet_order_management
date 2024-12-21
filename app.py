
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database initialization
DB_NAME = 'orders.db'

def init_db():
    """
    Initializes the SQLite database by creating the orders table if it doesn't already exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            item TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Fetches all orders from the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    conn.close()
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    """
    Creates a new order in the database.
    """
    data = request.get_json()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO orders (customer_name, item, quantity, status)
        VALUES (?, ?, ?, ?)
    ''', (data['customer_name'], data['item'], data['quantity'], 'Pending'))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Order created successfully'}), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Updates an existing order in the database.
    """
    data = request.get_json()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE orders
        SET customer_name = ?, item = ?, quantity = ?, status = ?
        WHERE id = ?
    ''', (data['customer_name'], data['item'], data['quantity'], data['status'], order_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Order updated successfully'})

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Deletes an order from the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM orders WHERE id = ?', (order_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Order deleted successfully'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
