#Programming exercises chapter 3
# exercise 4
# A Program to determine the distance of lightning

def main():
    print("This program calculates the distance of a lightning strike")
    speed = 1100
    mile = 5280
    time = eval(input("Enter the time elapsed between the flash and the sound of thunder:"))

    distance = speed * time 
    miles = distance // mile
    feet = distance % mile
    print("The lightning is about",miles,"miles and", feet, "feet away.")
main()
