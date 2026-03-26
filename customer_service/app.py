from flask import Flask, jsonify
import os

app = Flask(__name__)

customers = {
    1: {"name": "Arushi", "orders": [101,102]},
    2: {"name": "Rahul", "orders": [103]}
}

@app.route("/")
def home():
    return "Customer Service Running"

@app.route("/customers/<int:customer_id>/orders")
def get_orders(customer_id):

    customer = customers.get(customer_id)

    if customer:
        return jsonify(customer)
    else:
        return {"message":"Customer not found"},404


if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0", port=port)