# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [85, 90, 78, 92]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display data
print("Dataset:")
print(df)

# Line Graph
plt.plot(df['Name'], df['Marks'])
plt.title("Line Graph - Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()

# Bar Chart
plt.bar(df['Name'], df['Marks'])
plt.title("Bar Chart - Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.pie(df['Marks'], labels=df['Name'], autopct='%1.1f%%')
plt.title("Pie Chart - Marks Distribution")
plt.show()

# Histogram
plt.hist(df['Marks'])
plt.title("Histogram - Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
