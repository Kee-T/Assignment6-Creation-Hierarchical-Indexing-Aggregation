# Part 4a
DF1 = pd.DataFrame({'S1': S1, 'S2': S2, 'S3': S3, 'S4': S4})
DF1

# Part 4b
DF2 - cannot do, unable to guarntee any order for the sets

# Part 4c
DF3 = pd.DataFrame(
    [["a","e","i","m"],
     ["b","f","j","n"],
     ["c","g","k","o"],
     ["d","h","l","p"]],
    index=[10,20,30,40],
    columns=["S1","S2","S3","S4"]
)
DF3


# Part 4d
DF4 = pd.DataFrame(
    np.array([
        ["a","e","i","m"],
        ["b","f","j","n"],
        ["c","g","k","o"],
        ["d","h","l","p"]
    ]),
    index=[10,20,30,40],
    columns=["S1","S2","S3","S4"]
)
DF4

# Part 4e
DF5 = pd.DataFrame({
    "S1": {10:"a",20:"b",30:"c",40:"d"},
    "S2": {10:"e",20:"f",30:"g",40:"h"},
    "S3": {10:"i",20:"j",30:"k",40:"l"},
    "S4": {10:"m",20:"n",30:"o",40:"p"}
})
DF5

# Part 4f
DF6 = pd.DataFrame([
    {"S1":"a","S2":"e","S3":"i","S4":"m"},
    {"S1":"b","S2":"f","S3":"j","S4":"n"},
    {"S1":"c","S2":"g","S3":"k","S4":"o"},
    {"S1":"d","S2":"h","S3":"l","S4":"p"}
], index=[10,20,30,40])
DF6


# Part 4g
DF7 = pd.DataFrame({
    "S1":["a","b","c","d"],
    "S2":["e","f","g","h"],
    "S3":["i","j","k","l"],
    "S4":["m","n","o","p"]
}, index=[10,20,30,40])
DF7





# Part 5
DF2 = DF3.copy()

DF_concat = pd.concat([DF1, DF2])
DF_concat



# Part 6
DF_concat.insert(0, "S0", [1,2,2,3,3,4,4,5])
DF_concat


# Part 7
DF_hier = DF_concat.set_index("S0", append=True)
DF_hier

# Part 8
DF_group_index = DF_hier.groupby(level=[0,1]).agg(lambda x: ''.join(x))
DF_group_index


# Part 9
DF_group_S0 = DF_concat.groupby("S0").agg(lambda x: ''.join(x))
DF_group_S0
