# Break << based on condition it will kick u out of loop
for i in range(10):

    print(i)
    # pass << it will skip the required no and print the other nos
    for i in range(10):
        if i == 5:
            pass
        else:
            print(i)
