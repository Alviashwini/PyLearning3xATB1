def make_pizza(*toppings):
    print(toppings)


Ashwini = make_pizza("olives")
Sonakshi = make_pizza("tomato", "sweetcorn")
Pravash = make_pizza("mushroom", "pepper")


def make_pizza(*toppings):
    for topin in toppings:
        print(topin, end="\n")


Ashwini = make_pizza("olives")
Sonakshi = make_pizza("tomato", "sweetcorn")
Pravash = make_pizza("mushroom", "pepper")
