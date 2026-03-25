import pandas as pd
import numpy as np

# i. (set)
set = pd.Series({'a', 'b', 'c', 'd'})
set

# ii. (list)
list = pd.Series(['a', 'b', 'c', 'd'])
list

# iii. (array)
data = np.array({'a', 'b', 'c', 'd'})
array = pd.Series(data)
array

# iv. (dictionary)
# key becomes the index so 0, 1, 2, 3
dict = pd.Series({0: 'a', 1: 'b', 2: 'c', 3: 'd'})
dict