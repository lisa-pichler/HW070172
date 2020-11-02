# Programming exercises chapter 5
# exercise 10
# A program that calculates the averages length of words in a sentence

def main():
    print("This program calculates average lengths of words in a sentence")
    sentence = input("Please enter a sentence: ")

    count = 0
    for string in sentence.split():
       words = count + 1
       letters = count + len(string)
       length = letters / words
    print("The average length of the words in your sentence is:", length)
main()
