# Programming exercises chapter 7
# exercise 1

def main():
    print("This is a program to calculate total wages for the week")
    hours = eval(input("Enter the numbers you have worked: "))
    payment = eval(input("Enter your hourly wage: "))

    if hours <= 40:
        weeklywage = hours * payment 
    else:
        weeklywage = hours * payment + (hours - 40) *1.5 * payment
    print("Your weekly wage is:", weeklywage)
main()
