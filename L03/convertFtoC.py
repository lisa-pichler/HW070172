# convertFtoC
# A program that converts temperatures from Fahrenheit to Celsius 

def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 5 * (fahrenheit - 32) / 9
    print("The temperature is", celsius, "degrees celsius")
main()