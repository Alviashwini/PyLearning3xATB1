# List
# shopping list
# add, remove, update, view, exit items of list
shopping_list = ["milk", "bread", "butter", "poha", "dosa"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list[-3])
# Adding items in the end is append
shopping_list.append("curd")
print(shopping_list)
# updating item in middle or anywhere
shopping_list.insert(3, "jam")
print(shopping_list)
# extend means add multiple items in the end
shopping_list.extend(["salt", "chips"])
print(shopping_list)
shopping_list.remove("bread")
print(shopping_list.pop())
print(shopping_list)
my_list = [1, 2, 3, 4, True, 2.16, "Amit"]
print(type(my_list))
