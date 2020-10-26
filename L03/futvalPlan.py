# futval.py
# A program to compute the value of an investment
# carried 10 years into the future
def main():
    print("This program calculates the future value")
    print("of an investment plan.")
    
    for i in range(5):
        principal = eval(input("Enter the principal: "))
        apr = eval(input("Enter the annunal interest rate: "))
        x = eval(input("Enter the years of investment: "))

 
    for i in range(x):
        principal = principal * (1 + apr + x)

    print("The value in", x , "years is:", principal)
main()
