import pandas as pd
import random

# Sample names and surnames
names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Chris", "Jessica", "Brian", "Laura"]
surnames = ["Doe", "Smith", "Johnson", "Davis", "Brown", "Wilson", "Garcia", "Martinez", "Rodriguez", "Hernandez"]
partitions = ["r1", "r2", "r3"]

# Generate random data
data = {
    "Name": [random.choice(names) for _ in range(9000000)],
    "Surname": [random.choice(surnames) for _ in range(9000000)],
    "Partition": [random.choice(partitions) for _ in range(9000000)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel file
df.to_excel("random_data5.xlsx",index=False)