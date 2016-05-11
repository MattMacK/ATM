from Customer import Customer

customers = []
john = Customer(name="john", account=1234, funds=128.00)
bob = Customer(name="bob", account=1234, funds=128.00)
customers.append(john)
customers.append(bob)


def check_customers(customer_list, new_name):
    for customer in customer_list:
        if customer.name == new_name:
            customer.deposit_funds()
            break
        else:
            print("That account does not exist.")


def print_customers():
    for customer in customers:
        print(customer.name)


done = False
while not done:
    print("Welcome to your local bank terminal.")
    print("Please read the below options and make your choice.")
    print("1. Create a new account.\n"
          "2. Print list for existing accounts.\n"
          "3. Check balance for existing account.\n"
          "4. Deposit funds for existing account.\n"
          "5. Withdraw funds for existing account\n"
          "99. Quit")
    selection = int(input("Selection: "))
    if selection == 99:
        done = True
    elif selection == 1:
        print("need to create a new account")
    elif selection == 2:
        print_customers()
    elif selection ==3:
        print('need to create a print')
    elif selection == 4:
        name = input("What is the name of the account you would like to check? ")
        check_customers(customers, name)
