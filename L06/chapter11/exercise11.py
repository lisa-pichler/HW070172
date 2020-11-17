# Programming exercises chapter 11
# exercise 11
# A program to **** instead of words with 4 digits

def main():
    fname = "Pichler.txt"
    infile = open(fname, "r")

    outfile = open("Pichler1.txt", "w")
    for line in infile:
        words = line.split()
        for i in range(len(words)):
            if len(words[i]) == 4:
                words[i] = "****"
        line = " ".join(words)
        print((line), file = outfile)
    infile.close()
    outfile.close()
main()