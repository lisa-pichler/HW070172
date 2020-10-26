# convert.py
# A program to convert Celsius temps to Fahrenheit
# a tabele for Celsius 10-100 and the equal Fahrenheit temp
def main():
    for i in range(11):
        celsius = i *10
        fahrenheit = 9/5 * celsius + 32
        print(celsius, " ", fahrenheit)
main()
