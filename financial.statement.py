import numpy as np

print("___Welcome to out financial statement apps!___")

print("___It has financial statement and Balance sheet___")

expenses_1 = {}


revenue = int(input("Please input the revenue of 1 month: "))

def statement():


    expenses = input("Please input the type of expenses: ")

    amount_expenses = int(input("Please input the amount expenses: "))

    expenses_1[expenses] = amount_expenses

    
statement()

add = input("Do you want to add expenses(yes/no)")

while add != "no":
    statement()
    add = input("Do you want to add expenses(yes/no)")
    if add == 'no':
        break

total = np.sum(list(expenses_1.values()))
net_profit = revenue - total

        
assets = {}

liabilities = {}

def assets_function():
    own_1 = input("Please input the things you own: ")

    amount_own = int(input(f"Please input the amount of {own_1} you own: "))

    assets[own_1] = amount_own

assets_function()

add = input("Do you want to add the assets(yes/no)")

while True:
    if add == "yes":
        assets_function()
        add = input("Do you want to add assets(yes/no): ")
    elif add == 'no':
        break

    
def sheet():
    
    owes = input("Please input the things you owes(the things you have to paid): ")

    amount_owes = int(input(f"Please input the amount of {owes} you owes: "))

    liabilities[owes] = amount_owes
    
sheet()

add = input("Do you want to add the liabilites(yes/no)")

while True:
    if add == "yes":
        sheet()
        add = input("Do you want to add liabilities(yes/no)")
    elif add == 'no':
        break

total_liabilities = np.sum(list(liabilities.values()))

total_assets = np.sum(list(assets.values()))

owners_equity = total_assets - total_liabilities

cash_operating = {}

investing_cash = {}

financing_cash = {}

def cash_operator():
    cash_making = input("Please tell us the what do you make: ")

    cash_made = int(input(f"Please tell us the what is the amount of cash {cash_making} you made: "))
     
    cash_operating[cash_making] = cash_made
    
cash_operator()    
 
continue_1 = input("Do you want to continue(yes/no): ")

while continue_1 == "yes":
    cash_operator()
    continue_1 = input("Do you want to continue(yes/no): ")
    break
    

def cash_investing():
    cash_investor = input("Please tell us the where did you invest the money: ")

    cash_choice = input(f"Please tell us that the Investor{cash_investor} has made money or take money (made/take): ")

    cash_investor_amount = int(input(f"Please tell us the amount of investor: "))
     
    if cash_choice == "take":
        cash_investor_amount = -cash_investor_amount
    
    investing_cash[cash_investor] = cash_investor_amount
    
cash_investing()    
 
continue_2 = input("Do you want to continue(yes/no): ")

while continue_2 == "yes":
    cash_investing()
    continue_2 = input("Do you want to continue(yes/no): ")
    break

def finance_activities():

    cash_activities = input("Please tell us the where did  the money go: ")

    cash_activities_choice = input(f"Please tell us that the Investor{cash_activities} has made money or take money (made/take): ")

    
    cash_activities_amount = int(input(f"Please tell us the amount of investor: "))

    if cash_activities_choice == "take":
        cash_activities_amount = -cash_activities_amount                         
    
    financing_cash[cash_activities ] = cash_activities_amount
    
finance_activities()    
 
continue_3 = input("Do you want to continue(yes/no): ")

while continue_3 == "yes":
    finance_activities()
    continue_3 = input("Do you want to continue(yes/no): ")
    break


sum_cash_operating = np.sum(list(cash_operating.values()))

sum_investing_cash = np.sum(list(investing_cash.values()))


sum_financing_cash = np.sum(list(financing_cash.values()))

print("___Net profit___")
print(f"The amount of net profit business has done is {net_profit}")

print("___Expenses___")
for owes_1, amount in expenses_1.items():
    print(f"The amount of expenses business has done is {owes_1} The Amount you own {amount}")

print("___owners_equity___")
print(f" The amount of net owner equity you earn is {owners_equity}")

print("____Assets____")
for own, amount in assets.items():
    print(f"The things you own are {own} The Amount you own {amount} ") 

print("____-Liabilities_____")
for owes_1, amount in liabilities.items():
    print(f"The things you owes are {owes_1} The Amount you own {amount} ") 

print("___Cash operating___")
for sum, cash in  cash_operating.items():
    print(f"The things you made are {sum} and and amount is {cash}")
print(f"The cash is operating at {sum_cash_operating}")   

print("___Cash investing___")
for Invest_name, invest_amount in  investing_cash.items():
    print(f"The things you invest are {Invest_name} and and amount is {invest_amount}")
print(f"The cash amount of investing is  {sum_investing_cash}")  

print("___Cash Activities___")
for Money_go, going_amount in  financing_cash.items():
    print(f"The cash is going in {Money_go} and and amount is {going_amount}")
print(f"The cash is going at amount of {sum_financing_cash}")  


