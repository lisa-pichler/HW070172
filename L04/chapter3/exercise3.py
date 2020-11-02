#Programming exercises chapter 3
# Exercise 3
# A program to compute the molecular weight of a carbohydrate

def main():
    print("This is a program to calculate the weight of a carbohydrate")
    hydrogen = eval(input("Enter the number of hydrogen atoms: "))
    carbon = eval(input("Enter the number of carbon atoms: "))
    oxygen = eval(input("Enter the number of oxygen atoms: "))

    weight = hydrogen * 1.00794 + carbon * 12.0107 + oxygen * 15.9994
    print("The weight is:", weight)
main()