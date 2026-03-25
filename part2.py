import pandas as pd
import numpy as np

# i. (set)
set = pd.Series({'a', 'b', 'c', 'd'}, 
        index=[10, 20, 30, 40])
set

# ii. (list)
list = pd.Series(['a', 'b', 'c', 'd'], 
        index=[10, 20, 30, 40])
list

# iii. (array)
data = np.array({'a', 'b', 'c', 'd'})
array = pd.Series(data, 
        index=[10, 20, 30, 40])
array

# iv. (dictionary)
# key becomes the index so 10, 20, 30, 40
dict = pd.Series({10: 'a', 20: 'b', 30: 'c', 40: 'd'})
dict