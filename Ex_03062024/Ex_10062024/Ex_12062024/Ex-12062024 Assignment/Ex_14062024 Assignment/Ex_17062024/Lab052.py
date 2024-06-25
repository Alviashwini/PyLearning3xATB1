# print_argument another function
def print_argument(*args):
    for i in args:
        print(i, end=" ")

print_argument("Ashwini", "Sona", "Pravash")

def print_argument(*args):
    for i in args:
        print(i, end="\n")
print_argument("Ashwini", "Sona", "Pravash")