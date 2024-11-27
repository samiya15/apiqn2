from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

# In-memory storage for products
products = []

@app.route('/products', methods=['POST'])
def create_product():
    """
    Endpoint to create a new product.
    Expects JSON payload with 'name', 'description', and 'price'.
    """
    data = request.get_json()

    # Input validation
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input. Fields: name, description, price are required.'}), 400

    # Add new product
    product = {
        'id': len(products) + 1,  # Auto-increment ID
        'name': data['name'],
        'description': data['description'],
        'price': data['price']
    }
    products.append(product)
    return jsonify(product), 201  # Respond with 201 Created

@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve all products.
    """
    return jsonify(products), 200  # Respond with 200 OK

if __name__ == '_main_':
    app.run(debug=True)