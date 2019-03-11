fruits = "Apple", "Orange", "Banana", "Pear", "Melon", "Grape"

for fruit in fruits:
    print(fruit)
    dots = len(fruit)
    print(dots)
    for dot in range(0, dots):
        print('.', end="")
    print("")
