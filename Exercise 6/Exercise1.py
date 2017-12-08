word = input("enter a word:")

reverse_word = word[::-1]

if(reverse_word == word):
    print(str(word) + " is palindrome")
else:
    print(str(word) + " is not a palindrome")
    