# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load a built-in dataset
df = sns.load_dataset("tips")  # Dataset about restaurant tips

# Display first few rows
print(df.head())

# Set a theme for the plots
sns.set(style="whitegrid")

# 1. Scatter Plot - Total bill vs Tip
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex", style="time")
plt.title("Scatter Plot: Total Bill vs Tip")
plt.show()

# 2. Box Plot - Total bill by Day
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="day", y="total_bill", palette="Set2")
plt.title("Box Plot: Total Bill by Day")
plt.show()

# 3. Count Plot - Count of Customers by Day
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="day", hue="sex")
plt.title("Count Plot: Number of Customers by Day and Sex")
plt.show()

# 4. Violin Plot - Tip by Day
plt.figure(figsize=(6, 4))
sns.violinplot(data=df, x="day", y="tip", inner="quartile", palette="muted")
plt.title("Violin Plot: Tip Distribution by Day")
plt.show()

# 5. Pair Plot - All numerical columns
sns.pairplot(df, hue="sex", palette="coolwarm")
plt.suptitle("Pair Plot of All Numerical Columns", y=1.02)
plt.show()

# 6. Heatmap - Correlation Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="YlGnBu", linewidths=0.5)
plt.title("Heatmap: Correlation Matrix")
plt.show()
