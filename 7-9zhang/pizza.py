def make_pizza(size, *topppings):
    print(f"\nMakeing a {size}-inch pizza with the following toppings:")
    for topping in topppings:
        print(f"- {topping}")