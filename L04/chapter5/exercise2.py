# Programming exercises chapter 5
# exercise 2
# A Program to accept quiz scores and print out grades.

def main():
    print("This is a program to get grades from scores")
    score = eval(input("Please enter the quiz score: "))
    grades = ["F", "F", "D", "C", "B", "A"]
    print(grades[score])
main()

 