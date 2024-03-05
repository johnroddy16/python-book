# looping thru a dict:

name_and_num = {
    'michael': 4,
    'kevin': 90,
    'carolyn': 6,
    'mom': 2,
    'juan': 20,
}


for a in name_and_num:
    if name_and_num[a] > 4:
        print(a, name_and_num[a])