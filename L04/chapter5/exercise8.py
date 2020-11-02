# Programming exercises chapter 5
# Exercise 8
# Ceasar cipher continued

def main():
    print("A Program to decode caesar ciphers")
    name = input("Enter a name in lower cas:")
    key = eval(input("Enter the key. "))
    
    encoded_txt = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for ch in name:
        encoded_txt = encoded_txt + letters[(ord(ch)-97) + key % 52]
    print("Your encoded message is", encoded_txt)
main()

