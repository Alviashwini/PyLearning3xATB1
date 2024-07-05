my_dict = {
    'b': 2,
    'c': 4,
    'a': 3
}
# to find a key
for k,v in my_dict.items():
    if k == 'b':
        print("key with the name b")

    op = 'b' in my_dict
    print(op)