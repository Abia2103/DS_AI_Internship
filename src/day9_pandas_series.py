#Task 1: The Product Catalog (Series Creation & Indexing)
import pandas as pd
product = pd.Series([700, 150, 300], index=['Laptop', 'Mouse', 'Keyboard'])
print(product)
print(f"Price of Laptop: {product['Laptop']}")
print(f"First two products:\n{product[:2]}")

#Task 2: The Grade Filter (Boolean Masking & Missing Data)
grades = pd.Series([85, None, 92, 45, None, 78, 55])
print(f"isnull():\n{grades.isnull()}")
print(f"Filled series:\n{grades.fillna(0)}")
print(f"Filtered search:\n{grades[grades > 60]}")

#Task 3: The Username Formatter (Vectorized String Operations)
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
strip = usernames.str.strip()
print(f"Striped usernames:\n{strip}")
lower = strip.str.lower()
print(f"Lower case usernames:\n{lower}")
a = lower.str.contains('a')
print(f"Boolean result of the 'a' search:\n{a}")


