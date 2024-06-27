# Important question
# Lambda expression: it is used to do the task in one line.

def double_my_salary(salary):
    return salary * 2


new_salary = double_my_salary(200)
print(new_salary)

# lamba shoukd be done in 1 line so follow this

f_double_salary = lambda salary: salary * 2
print(f_double_salary(100))
