def outer_function():
    var1 = 30


def inner_function():
    print(var1)
    inner_function()


outer_function()
