# Programming exercises chapter 7
# Exercise 4

def main():
    print("A program that calculates the credits and class standings")
    x = eval(input("How many credits do you have? "))

    if x < 7:
        print('Freshman')
    elif 7 <= x <16:
        print('Sophomore')
    elif 16 <= x <26:
        print('Junior')
    elif x >= 26:
        print('Senior')
main()
   
