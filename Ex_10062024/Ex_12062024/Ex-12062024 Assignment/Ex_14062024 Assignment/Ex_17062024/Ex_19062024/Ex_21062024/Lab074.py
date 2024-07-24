# unpacking of tuple
# append will not work bcz of immutable nature of tuple
a, b, c = (12, 34, 56)

t = (12, 34, 56)
# t.append()
# other way of adding new tuple t +4, comma should be used here or else concatenation error occurs.
new_t = t + (4,)
print(new_t)
# or u can convert list into tuple.
my_list = list(t)
print(my_list)
my_list.append(5)
new_t2 = tuple(my_list)
print(new_t2)
