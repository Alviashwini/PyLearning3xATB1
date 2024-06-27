# Tuples - collection of items. it is also a list but it will be in round brackets.
# immutable means objects can't be changed.
# diff b/w list and tuple
# list
my_list = [1, 2, 3, 4, 5]
print(id(my_list))
my_list[0] = 21  # mutable
print(my_list)
print(id(my_list))
# Tuple
my_tuple = (1, 2, 3, 4, 5, 5)
my_tuple [0] = 21 # Immutable
print(my_tuple)
