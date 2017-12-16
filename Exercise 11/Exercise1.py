def isPrime(number):
    if(number > 0):
        for x in range(2, number - 1):
            if number % x != 0:
                continue
            elif number % x == 0:
                s = "The number is not prime."
        s = "The number " + str(number) + " is prime."        
    elif(number == 0):
        s = "The number is not prime."
    else:
        s = "The number is not prime."
    return s

number = int(input("Give me a number:"))
print(isPrime(number))


