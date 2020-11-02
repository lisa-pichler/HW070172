#Programming exercises chapter 5
# Exercise 4
# A program to create Acronyms

def main():
    print("This program creates Acronyms")

    phrase = input("Please enter a phrase: ")
    words = []

    for string in phrase.split():
        first = string[0].upper()
        words.append(first)
    acronym = "".join(words)
    print(acronym)
main()
