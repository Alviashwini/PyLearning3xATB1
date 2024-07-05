# Map
# pick 1 item and apply the function
# gives the same no of elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def double_me(num):
    return num * 2


new_list_double = map(double_me, numbers)
print(list(new_list_double))
# or we can use lambda expression for double me directly without using def function
new_list_double = map(lambda n: n * 2, numbers)
print(list(new_list_double))


# filters
# pick 1 item if true keep it, false remove it.
# it can give less no of items as compared to actual list.

def even_given(num):
    return num % 2 == 0


new_filtered_list = list(filter(even_given, numbers))
print(new_filtered_list)
# or we can use lambda expression for even giver directly without using def function
new_filtered_list = list(filter(lambda x: x % 2 == 0, numbers))
print(new_filtered_list)



