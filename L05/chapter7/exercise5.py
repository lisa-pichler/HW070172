# Programming exercises chapter 7
# exercise 5

def main():
    weight = eval(input("Please enter your weight in pounds: "))
    height = eval(input("Please enter your height in inches: "))

    BMI = (weight * 720) / height**2
    if 19 <= BMI <= 25:
        print("Your BMI is within the healty range")
    elif BMI < 19:
        print("Your BMI is below the healty range")
    elif BMI > 25:
        print("Your BMI is higher than the healty range")
main()