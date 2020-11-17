# Programming exercises chapter 8
# exercise 1
# Fibonacci again 

def main(): 
    n = eval(input("What Fibonacci number do you want to see?")) 
    count = 0
    x = 1
    y = 0 
    while count < n:
        count = count + 1
        z = x + y
        x = y
        y = z 
    print("Your Fibonacci number is", z)
main()
