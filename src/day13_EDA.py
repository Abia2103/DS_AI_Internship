#Task 1: The Distribution Deep-Dive (Univariate Analysis)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
df = pd.read_csv("Housing.csv")
plt.figure()
sns.histplot(x=df["price"],kde=True)
plt.title("Price histograam")
plt.show()
print("Skewness: ",df["price"].skew())
print("Kurtosis: ",df["price"].kurt())
plt.title("Count plot of Furnishing status")
sns.countplot(x="furnishingstatus",data=df)
plt.show()


#Task 2: The Relationship Map (Bivariate Analysis)
sns.scatterplot(x="area",y="price",data=df)
plt.title("Area vs Price scatter plot")
plt.show()
sns.boxplot(x=df["bedrooms"],y=df["price"])
plt.title("Price increases as number of bedrooms increase, then decreases slightly for more than 5")
plt.show()


#Task 3: The Pattern Finder (Correlation & Outliers)
corr=df.corr(numeric_only=True)
print(corr)
print("No variables with a high correlation of <0.8")
sns.heatmap(corr, annot=True)
plt.title("Heatmap")
plt.show()

sns.boxplot(x=df["price"])
plt.title("Outliers in price")
plt.show()


