# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell
#changed for chapter 6 to add warnings
def main():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print ("The temperature is", fahrenheit, "degrees Fahrenheit.")
    # Print warnings for extrem temps.
    if fahrenheit > 90:
        print("It is really hot out there. Be careful.")
    if fahrenheit < 30:
        print("Brrr. Be sure to dress warmly.")
main()
 