# Programming exercises chapter 5
# exercise 9
# A program that counts the numbers of words in a sentence

def main():
    print("A program that counts the numbers of words")
    words = input("Enter a sentence: ")

    count = 0 
    for string in words.split():
       count = count + 1
    print("There are", count, "words in your text")
main()