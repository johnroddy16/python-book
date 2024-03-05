# playing with .items():

name_and_num = {
    'michael': 206_418_8234,
    'kevin': 9072284934,
    'carolyn': 2062954876,
    'mom': 2063567535,
    'juan': 2063802424,
}

c = name_and_num.get('michael')  # risky without the default output but words if the key is there
print(c)

d = name_and_num.get('dad')  # will not throw an error but will return None
print(d)

e = name_and_num.get('dad', 0)  # will return 0
print(e)