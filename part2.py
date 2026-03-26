import pandas as pd
import numpy as np

# i. (set)
# needs to convert set to list first because set is unordered and does not support indexing
set = pd.Series((list{'a', 'b', 'c', 'd'}, 
        index=[10, 20, 30, 40]))
print(set)

# ii. (list)
list = pd.Series(['a', 'b', 'c', 'd'], 
        index=[10, 20, 30, 40])
print(list)

# iii. (array)
array = (['a', 'b', 'c', 'd'])
data = pd.Series(array, 
        index = [10, 20, 30, 40])
print(data)

# iv. (dictionary)
# key becomes the index so 10, 20, 30, 40
dict = pd.Series({10: 'a', 20: 'b', 30: 'c', 40: 'd'})
print(dict)
