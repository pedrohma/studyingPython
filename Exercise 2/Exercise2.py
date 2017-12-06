number = input("Enter a number: ")
rest = int(number) % 2
if rest > 0:
    print(str(number) + " is an odd number.")
else:
    print(str(number) + " is an even number.")