# Programming exercises chapter 6
# exercise 2
# A program to print the lyrics for ten verses of The Ants Go Marching 

def march():
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    activities = ["suck his thumb", "tie his shoe", "climb a tree", "shut the door", "take a dive",
    "pick up sticks","pray to heaven", "roller skate", "check the time", "shout The End"]
    for i in range(10):
        print("The ants go marching {0} by {0}, hurrah! hurrah!".format(str(numbers[i])))
        print("The ants go marching {0} by {0}".format(str(numbers[i])))
        print("The little one stops to {0}".format(str(activities[i])))
        print ("And they all go marching down to\nThe ground\nTo get out of the rain,\nBOOM BOOM BOOM")
def main():
    march()
main()