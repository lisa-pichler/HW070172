# Programming exercises chapter 5
# exercise 7
# A program to decode Caesar ciphers
def main():
    print("This is a program to decode Caesar ciphers")
    text = input("Enter a message you would like to encode: ")
    key = eval(input("Enter the value of the key: "))

    encoded_txt = ""
    for ch in text:
        encoded_txt = encoded_txt + (chr(ord(ch) + key))
    print("Your encoded message is {0}.".format(encoded_txt))
main()
