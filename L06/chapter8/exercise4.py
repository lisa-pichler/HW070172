# Programming exercises chapter 8
# exercise4.py
#Syracuse sequence 

def main():
    value = eval(input("Enter your starting number for the string: "))

    print(str(value) + ",", end = "")
    while value != 1:
        if value % 2 == 0:
            value = value // 2
        else:
         value = 3 * value + 1
        if value != 1:
            print(str(value) + ",",end= "")
        else:
            print(1)
main()

