# Programming exercises chapter 5
# exercise 5 
# A program to determine the numeric value of a name 

def main():
    print("This program dtermines a numeriv value of a name")
    name = input("Please enter a name: ")

    sum = 0 
    for ch in name: 
        sum = int(ord(ch)) + sum - 96 
    print("The numeric value for", name, "is", sum)
main()
