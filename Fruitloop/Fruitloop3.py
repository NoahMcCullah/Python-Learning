fruits = "Apple", "Orange", "Banana", "Pear", "Melon", "Grape"

for fruit in fruits:
    print(fruit)
    dots = fruits.index(fruit)
    print(dots)
    for x in range(0, dots):
        dot = '.'
        print(dot, end="")
    print("")
