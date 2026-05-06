import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print(df)

plt.bar(df['Name'], df['Marks'])
plt.title("Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")

plt.show()   
