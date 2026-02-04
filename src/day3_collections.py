#Task-1: The Inventory Manager
inventory = ["Apples", "Bananas", "Carrots", "Dates"]
inventory.append("Eggs")
inventory.remove("Bananas")
inventory.sort()
print(inventory)

#Task-2: The Data Slicer
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print(f"First reading: {temperatures[0]}  Last reading: {temperatures[-1]} " )
print(f"Afternoon peak: {temperatures[3:6]}")
print(f"Last 3 hours: {temperatures[-3:]}")

#Task-3: The Immutable Config
screen_res = (1920, 1080)
#screen_res[0] = 1280
print("Tuples cannot be modified!")