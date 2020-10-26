# futval.py
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10 year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    rate = eval(input("Enter the number of times the interest is compounded: "))

    for i in range(10 * rate):
        principal = principal * (1 + (apr / rate))
    print("The value in 10 years is:", principal)
main()
