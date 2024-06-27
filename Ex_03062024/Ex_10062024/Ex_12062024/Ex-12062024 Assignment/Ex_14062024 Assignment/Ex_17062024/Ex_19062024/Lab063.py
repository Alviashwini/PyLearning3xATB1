# lambda arguments expression
def find_odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("odd")


find_odd_even(5)
# in lambda
check_even_odd = lambda num: "Even" if num % 2 == 0 else "odd"
print(check_even_odd(6))
