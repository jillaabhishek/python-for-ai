# import math
# math.sqrt(16)

# from math import sqrt, pi

# sqrt(16)
# pi

# Import entire module
# import random

# # Use module functions
# number = random.randint(1, 10)
# choice = random.choice(["apple", "banana", "orange"])


# import datetime

# today = datetime.date.today()  
# print(datetime.datetime.now())

# Operating system
# import os
# current_dir = os.getcwd()
# print(current_dir)


# Web requests
import requests

response = requests.get("https://api.example.com/data")
data = response.json()

# Data analysis
import pandas as pd

# Create a simple DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
print(data)
df = pd.DataFrame(data)
print(df)