import pandas as pd
dataset = pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/nba.csv')
print(dataset)
print("size: ",dataset.size)
print("shape: ",dataset.shape)
print("dimmension: ",dataset.ndim)

