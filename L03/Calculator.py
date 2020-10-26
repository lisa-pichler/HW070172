# An interactive Python calculator program
# The program should allow the user to type a mathematical expression, and then print the value

def main():
    print("This is an interactive Python calculator program.")
    for i in range(100):
        x = eval(input("Type a mathematical expression" +" " "or type a bad expression and make the program crash: "))
        print("this is your result:", x)
main()


