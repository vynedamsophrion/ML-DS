#Day-2

Preprocessing (Commit 1)

# Import pandas
import pandas as pd

# Create a simple dataset
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Display the dataset
print(df)

#Preprocessing (Commit 2)

# Add new column for age in months
df['Age_in_months'] = df['Age'] * 12

# Display the updated dataset
print(df)
