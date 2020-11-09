# Programming exercises chapter 7
# exercise 8
# A program to see if you are eligible as a Senitor or Us representative

def main():
    age = eval(input("Please enter your age: "))
    citizen = eval(input("Please enter how long you have been living in the US: "))

    if age >= 30:
        if citizen >=9:
            print("Yes you are eligible for the Senat and the House.")
        if citizen >= 7:
            print("You are eligible for the House.")
    elif 30 > age >= 25:
        if citizen >= 7:
            print("You are eligible for the House.")
    else:
        print("Sorry you are not eligible")
main()
