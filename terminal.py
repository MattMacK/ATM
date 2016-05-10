from Customer import Customer

customer = Customer(name="John",account=1234,funds=123.00)
customer.withdraw_funds()
print(customer.funds)