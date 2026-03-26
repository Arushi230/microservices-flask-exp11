# Microservice Backend - Flask

This project implements two microservices using Python Flask.

Services:
1. Customer Service – Fetch customer orders
2. Order Service – Update order status

Data Storage:
In-memory variables only.

Tools Used:
Python
Flask
Postman
Render

Customer API
GET /customers/{id}/orders
{
    "customer_id": 1,
    "orders": [
        101,
        102
    ]
}
Order API
PUT /orders/{id}
{
    "new_status": "Shipped",
    "order_id": 101
}
# Learning Outcomes
Learnt about backend resources
Learnt about postman commands

# Screenshots
![customer service by GET](<Screenshot (368).png>)
![order service by PUT](<Screenshot (369).png>)
