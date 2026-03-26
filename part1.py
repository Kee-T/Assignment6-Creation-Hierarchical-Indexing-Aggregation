import pandas as pd
import numpy as np

# i. (set)
# needs to convert set to list first because set is unordered and does not support indexing
set = pd.Series(list({'a', 'b', 'c', 'd'}))
print(set)

# ii. (list)
list = pd.Series(['a', 'b', 'c', 'd'])
print(list)

# iii. (array)
array = np.array(['a', 'b', 'c', 'd'])
data = pd.Series(array)
print(data)

# iv. (dictionary)
# key becomes the index so 0, 1, 2, 3
dict = pd.Series({0: 'a', 1: 'b', 2: 'c', 3: 'd'})
print(dict)
