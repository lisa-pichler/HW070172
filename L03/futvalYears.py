# futval.py
# A program to compute the value of an investment
# carried .. years into the future
def main():
    print("This program calculates the future value")
    print("of an investment.")
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annunal interest rate: "))
    x = eval(input("Enter the years of investment: "))

    for i in range(x):
        principal = principal * (1 + apr)

    print("The value in", x, "years is:", principal)
main()
