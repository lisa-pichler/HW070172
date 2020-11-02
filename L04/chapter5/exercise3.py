# Programming exercises chapter 5
# Exercise 3
# A program that accepts an exam score as input and prints out the grade.

def main():
    print("A program that translates scores into grades")

    score = eval(input("Enter your a score: "))

    grades = ["F", "F", "F", "F","F", "F", "D","C", "B", "A"]

    grade = grades[int(score/10)]
   
    print("Your score is", grade)
main()
 