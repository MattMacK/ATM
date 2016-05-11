class Customer:



    def __init__(self, name, account, funds=0.0):
        self.name = name
        self.account = account
        self.funds = funds

    def return_name(self):
        return self.name

    def print_funds(self):
        print(self.funds)

    def print_user_info(self):
        print("Customer: ", self.name)
        print("Current Balance: ", self.funds)

    def deposit_funds(self):
        amount = float(input("Please input the amount of money you want to enter: "))
        self.funds += amount

    def withdraw_funds(self):
        done = False
        while not done:
            print("You currently have $", self.funds)
            amount = input("How much would you like to withdraw: ")
            if not amount.isalpha():
                if amount > self.funds:
                    print("Insufficient funds")
                elif amount <= self.funds:
                    self.funds -= amount
                    print("You have withdrawn $", amount, '.')
                    print("Your remaining balance is $", self.funds)
                    done = True
            else:
                print("Invalid entry.")

