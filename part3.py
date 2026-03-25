import pandas as pd

# i. (set)
S1 = pd.Series({'a', 'b', 'c', 'd'}, 
        index=[10, 20, 30, 40])
S1

# ii. (list)
S2 = pd.Series(['e', 'f', 'g', 'h'], 
        index=[10, 20, 30, 40])
S2

# iii. (array)
data = ({10: 'i', 20: 'j', 30: 'k', 40: 'l'})
S3 = pd.Series(data)
S3

# iv. (dictionary)
# key becomes the index so 10, 20, 30, 40
S4 = pd.Series({10: 'm', 20: 'n', 30: 'o', 40: 'p'})
S4