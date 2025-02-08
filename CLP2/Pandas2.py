import pandas as pd
import numpy as np

data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile', 'Tablet'],
    'Quantity': [2, 5, np.nan, 1, np.nan, 4],  
    'Price': [800, 500, 300, 800, 500, np.nan]  
}

df = pd.DataFrame(data)

print("Original DataFrame with missing values:")
print(df)

df_filled = df.copy()

df_filled['Quantity'] = df_filled['Quantity'].fillna(df_filled['Quantity'].mean())
df_filled['Price'] = df_filled['Price'].fillna(df_filled['Price'].mean())

print("\nDataFrame after filling missing values with column-wise means:")
print(df_filled)
