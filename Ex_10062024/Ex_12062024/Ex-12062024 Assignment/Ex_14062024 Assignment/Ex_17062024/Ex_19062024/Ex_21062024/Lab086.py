Ashwini_details = \
    {'name': 'Ashwini',
     'age': 28,
     'is female': True,
     'address': 'paris'}

print(Ashwini_details.get("address"))
print(Ashwini_details["address"])
print(Ashwini_details.values())
print(Ashwini_details.keys())
my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}
print(my_dict)
print(len(my_dict))
# conversion of dict to list
print(list(my_dict.keys()))
print(list(my_dict.values()))
# to go one by one
for i in list(my_dict.keys()):
    print(i)
for k,v in my_dict.items():
    print(k,v)
