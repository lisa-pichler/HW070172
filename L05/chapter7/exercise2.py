# Programming exercises chapter 7
# exercise 2

def main():
    score = eval(input("Enter your points: "))

    if score == 5:
        print("A")
    elif score == 4:
        print("B")
    elif score == 3:
        print("C")
    elif score == 2:
        print("D")
    elif score <= 1:
        print("F")
main()
