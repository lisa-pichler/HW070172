# chapter 8
# average7.py

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r') 
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            total = total + float(xStr)
            count = count + 1
        line = infile.readline()
    print("\nThe average of the number is", total / count)
main()

