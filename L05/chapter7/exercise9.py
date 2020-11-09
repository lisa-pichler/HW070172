# Programming exercises chapter 7
# exercise 9
# A program for computing easter dates in the years 1982-2048

def main():
    year = eval(input("Enter a year between 1982 and 2048: "))
    if 1982 <= year <= 2048:
        a = year % 19
        b = year % 4
        c = year & 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7 

        day = 22 + d + e
    else: 
        print("Please enter a year between 1982 - 2048: ")
   
    if day > 31:
     print("Easter falls into April", day - 31, "in the year", year)
    else:
      print("Easter falls into March", day, "in the year", year)
main()
