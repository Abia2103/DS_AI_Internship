#Task 2: The Comparison Dashboard (Bar Charts & Subplots)
import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home'] 
values = [300, 450, 200]
plt.subplot(1, 2, 1)
plt.bar(categories, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar chart")
plt.subplot(1, 2, 2)
plt.plot([1, 2, 3, 4, 5],[50, 55, 65, 70, 75])
plt.xlabel("Months")
plt.ylabel("No. of units sold")
plt.title("Line plot")
plt.tight_layout()