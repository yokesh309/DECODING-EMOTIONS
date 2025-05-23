# -*- coding: utf-8 -*-
"""Week 3-task 1-05.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yFYuEb5v52WiEGPBRWlHZxYc0J3alVVI

5.Data manipulation with pandas
"""

import pandas as pd

# Sample patient data
data = {
    'Patient_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Cholesterol': [180, 220, 190, 250, 210]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set cholesterol threshold
threshold = 200

# Filter patients above the threshold
high_cholesterol_patients = df[df['Cholesterol'] > threshold]

# Display results
print(high_cholesterol_patients)