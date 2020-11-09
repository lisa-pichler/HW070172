# Programming exercises chapter 7
# exercise 6

def main():
    print("A program that accepts a speed limit and prints if it was legal or the amount of fine to pay")
    speedlimit = eval(input("Enter the speed limit: "))
    speed = eval(input("Enter the clocked speed: "))

    if speed <= speedlimit:
        print("Yours speed was legal")
    elif speedlimit < speed < 90:
        fine = 50 + (speed - speedlimit) * 5
        print("Your fine is:", fine)
    elif speedlimit < speed > 90:
        fine = 50 + ((speed - speedlimit) * 5) + 200
        print("Your fine is:", fine)
main()
