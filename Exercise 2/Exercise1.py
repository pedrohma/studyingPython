num = int(input("Enter a number:"))
x = num % 4
if x == 0:
    print(str(num) + " is multiple of 4.")
elif x > 0:
    print(str(num) + " is an odd number.")
else:
    print(str(num) + " is an even number.")
