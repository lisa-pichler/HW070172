# programming exercises chapter 3
# exercise 2
# A program that calculates the cost per square inch of a pizza
#changes for programming exercise 5, chapter 6
import math
def pizzaAr(diameter):
    pizza = math.pi * (diameter/2)**2
    return pizza
def pizzaprice(price,pizza):
    pricepsq = price / pizza
    return pricepsq

def main():
    diameter = eval(input("Enter a diameter of the pizza in inches: "))
    price = eval(input("Enter the price of the pizza in Euro: "))
    pizza = pizzaAr(diameter)
    pricepsq = pizzaprice(price, pizza)
    print("The cost per square inch is:", pricepsq)
main()