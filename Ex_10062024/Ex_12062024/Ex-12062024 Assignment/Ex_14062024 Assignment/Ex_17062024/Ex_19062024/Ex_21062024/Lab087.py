my_dict = {'a': 11, 'b': 12, 'c': 63, 'a': 95}
print(my_dict)
# for key, value
for k, v in my_dict.items():
    print(k, v)

from collections import OrderedDict
od = OrderedDict()
od['a'] = 45
od['d'] = 89
od['c'] = 32
od['b'] = 67
print(od)
# Dict will not keep the order of insertion
# OrderedDict will keep the order of insertion


