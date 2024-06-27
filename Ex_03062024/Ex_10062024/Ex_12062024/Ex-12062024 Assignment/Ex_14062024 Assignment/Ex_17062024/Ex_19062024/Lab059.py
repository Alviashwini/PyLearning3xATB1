# list is collection of items
numbers = [1, 2, 3]


def do_something(numbers):
    numbers.append(4)
    return numbers


l = do_something(numbers)
print(l)


def do_something(numbers):
    numbers.append(5)
    numbers[1] = 30
    return numbers


l = do_something(numbers)
print(l)
