# chapter 8
# average6.py

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r') 
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        total = total + float(line)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the number is", total / count)
main()
