from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory order data
orders = {
    101: {"status": "Pending"},
    102: {"status": "Pending"},
    103: {"status": "Pending"}
}

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):

    if order_id not in orders:
        return jsonify({"message": "Order not found"}), 404

    data = request.json
    orders[order_id]["status"] = data.get("status")

    return jsonify({
        "order_id": order_id,
        "new_status": orders[order_id]["status"]
    })

if __name__ == '__main__':
    app.run(port=5001)