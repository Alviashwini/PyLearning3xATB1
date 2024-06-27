# without using forloop we can use this map function to execute any program using like +,-, /
# power *
# def double_item(num):
#    return num * 2
# instead of above 3rd line we can use lambda function
my_list = [1, 2, 3, 4, 5]
double_item = lambda num: num ** 2
double_item = list(map(double_item, my_list))
print(double_item)
# or
double_item = list(map(lambda num: num ** 2, my_list))
print(double_item)
# or
print(list(map(lambda num: num ** 2, [1, 2, 3, 4, 5])))
