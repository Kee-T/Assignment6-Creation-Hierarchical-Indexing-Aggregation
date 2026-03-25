import pandas as pd
import numpy as np

# i. (set)
s = pd.Series({'a', 'b', 'c', 'd'})
s

# ii. (list)
s = pd.Series(['a', 'b', 'c', 'd'])
s

# iii. (array)
arr = np.array({'a', 'b', 'c', 'd'})
s = pd.Series(arr)
s

# iv. (dictionary)
s = pd.Series({0: 'a', 1: 'b', 2: 'c', 3: 'd'})
s