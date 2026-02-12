#Task 1: The Integrity Audit (Missing Values & Duplicates)
import pandas as pd
df = pd.read_csv("customer_orders.csv")
print("Initial shape: ",df.shape)
print("Number of duplicates: ",df.duplicated().sum())
print(df.isna().sum())
df=df.drop_duplicates()

df["Name"]=df["Name"].fillna("Unknown")
df["Price"]=df["Price"].fillna(df["Price"].median())
df["Payment_mode"]=df["Payment_mode"].fillna(df["Payment_mode"].mode()[0])
df["Location"]=df["Location"].fillna(df["Location"].mode()[0])

print("Cleaned data:")
print(df)

print("Final shape: ",df.shape)

#Task 2: The Type Fixer (Data Type Conversion)

data = pd.read_csv("customers.csv")
print(data["Price"])
data["Price"] = data["Price"].str.replace("$",'')
data["Price"]=data["Price"].astype(float)
data["Date"] = pd.to_datetime(data["Date"])
print("Final data types:\n",data.dtypes)

# Task 3: The Categorical Standardizer (String Cleaning)
d = pd.read_csv("customer.csv")
print("Initial locations:\n",d["Location"])
d["Location"] = d["Location"].str.strip()
d["Location"] = d["Location"].str.lower()
unique = d["Location"].unique()
print("Unique locations")
print(unique)
