import pandas as pd

# i. (set)
# needs to convert set to list first because set is unordered and does not support indexing
S1 = pd.Series(list({'a', 'b', 'c', 'd'}), 
        index=[10, 20, 30, 40])
S1

# ii. (list)
S2 = pd.Series(['e', 'f', 'g', 'h'], 
        index=[10, 20, 30, 40])
S2

# iii. (array)
array = (['i', 'j', 'k', 'l'])
S3 = pd.Series(array, 
        index = [10, 20, 30, 40])
S3

# iv. (dictionary)
# key becomes the index so 10, 20, 30, 40
S4 = pd.Series({10: 'm', 20: 'n', 30: 'o', 40: 'p'})
S4
