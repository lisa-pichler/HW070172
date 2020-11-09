# Programming exercises chapter 7
# exercise 3

def main():
    score = eval(input("Please enter your score: "))
    
    if score >= 90:
        print("A")
    elif 90 > score >= 80:
        print("B")
    elif 80 > score >= 70:
        print("C")
    elif 70 > score >= 60:
        print("D")
    elif 60 > score:
        print("F")
main()