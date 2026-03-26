from flask import Flask,request,jsonify
import os

app = Flask(__name__)

orders = {
101:{"status":"Pending"},
102:{"status":"Pending"},
103:{"status":"Pending"}
}

@app.route('/')
def home():
    return "Order Service is running successfully"

@app.route("/orders/<int:order_id>",methods=["PUT"])
def update_order(order_id):

    if order_id not in orders:
        return {"message":"Order not found"},404

    data = request.json
    orders[order_id]["status"] = data["status"]

    return jsonify({
        "order_id":order_id,
        "new_status":orders[order_id]["status"]
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)