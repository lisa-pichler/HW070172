#Programming exercises chapter 3
# exercise 5
# A program to calculate the cost of an order at the Konditorei coffee shop.

def main():
    print("A calculation for the cost of an order at the Konditorei.")
    pound = eval(input("How many pounds of coffee are you ordering: "))

    total = pound * 10.50 + pound * 0.86 + 1.50
    print("The total cost is:", total, ("Euros"))
main()