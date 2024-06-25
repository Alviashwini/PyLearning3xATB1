# *args
print("Ashwini","Sona","Pravash","Praveen")

def sum_three(a, b, c):
    return a + b + c


result1 = sum_three(2,4,6)
print(result1)
result2 = sum_three(a=10, b=20, c=30)
print(result2)
result3 = sum_three(b=5, c=10, a=15)
print(result3)
result1 = sum_three(a=1, b=2, c=3)
result2 = sum_three(2, 3, 6)
result3 = sum_three(a=10, b=10, c=10)
print(result1,result2,result3)
