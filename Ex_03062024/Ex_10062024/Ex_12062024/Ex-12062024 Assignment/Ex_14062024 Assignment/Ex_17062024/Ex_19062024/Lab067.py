my_list = [1, 2, 3, 4, 5]
# temp_list = []
# for i in list:
#  temp = i*2
#    temp_list.append(temp)
# print(temp_list)
# map() function: it is also used to know double value
# map() function is to take each item from the list. execute the function on it.
# return same no of elements from list.
def double_item(num):
    return num * 2


double_list = list(map(double_item, my_list))
print(double_list)


def double_item(num):
    return num + 2


double_list = list(map(double_item, my_list))
print(double_list)
