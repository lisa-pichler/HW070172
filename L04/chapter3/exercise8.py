#programming exercises chapter 3
# exercise 8
# A program for the calucaltion of the easter date

def main():
    print("The Gregorian epact")
    year = int(input("Enter a 4-digit year: "))
    C = year // 100
    epact = (8 + (C//4) - C + ((8 * C+13) //25) + 11 * (year % 19)) % 30
    print("The value of the epact is", epact)
main()
