word = input("Type multiple words")

def reverseWords(word):
    array = word.split(" ")
    for i in array[::-1]:
        print(i)

reverseWords(word)