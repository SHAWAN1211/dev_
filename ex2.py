import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample email dataset created manually
data = {
    'text': [
        "Congratulations! You've won a prize. Click here to claim.",
        "Meeting scheduled for 10 AM tomorrow. Please confirm attendance.",
        "Get rich fast with this amazing scheme!!!",
        "Project update: tasks completed, deadline next week.",
        "Earn money from home, no experience needed!",
        "Reminder: doctor's appointment at 5 PM.",
        "URGENT! Your account has been compromised. Verify now.",
        "Hey, just checking in. How's everything going?",
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0]  # 1 = spam, 0 = ham
}

# Create DataFrame
df = pd.DataFrame(data)

# Show basic info
print("First few rows:")
print(df.head())

# Add email length column
df['length'] = df['text'].apply(len)

# Count labels
print("\nSpam vs Ham Counts:")
print(df['label'].value_counts())

# Plot label distribution
sns.countplot(x='label', data=df)
plt.title("Spam vs Ham Distribution")
plt.xticks([0, 1], ['Ham (0)', 'Spam (1)'])
plt.show()

# Plot email length distribution
sns.boxplot(x='label', y='length', data=df)
plt.title("Email Length by Spam/Ham")
plt.xticks([0, 1], ['Ham (0)', 'Spam (1)'])
plt.show()