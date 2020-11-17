# Programming exercises chapter 8
# exercise 3
# investment and while loop
def main():
    interest = eval(input("Please enter the annual interest rate: "))

    initial = 1
    year = 0

    while initial <  initial * 2:
        initial = initial * (1 + interest)
        year += 1
    print("The number of years it takes for your initial to double is:",year)
main()



    