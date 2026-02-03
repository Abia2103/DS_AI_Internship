#Task-1: The age in 2030 calculator
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hey {name} you will be {age+4} years old in 2030!")

#Task-2: The bill splitter
bill = float(input("Enter the total bill amount: "))
num = int(input("Enter the number of people: "))
share = bill/num
print(f"Total Bill: [{bill}]. Each person pays: [{share}]")
print(type(bill))
print(type(num))
print(type(share))

#Task-3: The raw data formatter
item_name = "socks"
quantity = 4
price = 120
in_stock = True
print(f"Item: {item_name}, Qty:{quantity}, Price: {price}, Available: {in_stock}")
print("Total cost: ",quantity*price)