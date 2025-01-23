import pandas as pd
import numpy as np

# Generate random data
np.random.seed(42)

data = {
    "Machine_ID": np.random.randint(1, 11, 1000),
    "Temperature": np.random.randint(60, 100, 1000),
    "Run_Time": np.random.randint(50, 200, 1000),
    "Downtime_Flag": np.random.choice([0, 1], size=1000)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('dataset/sample_data.csv', index=False)
print("Sample data generated and saved as 'sample_data.csv'.")
