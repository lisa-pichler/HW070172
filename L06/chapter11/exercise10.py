# Programming exercises chapter 11
#exercise 10
# sieve of eratosthenes

import math
def main():
    number = int(input("Please enter a number: "))
    primes = []
    for i in range(2,number+1):
         primes.append(i)
    i = 2
    while(i <= int(math.sqrt(number))):
        if i in primes:
            for x in range(i*2, number+1, i):
                if x in primes:
                    primes.remove(x)
        i = i+1
    print("All the prime numbers before",number,"are", primes)
main()

# does not remove stuff yet.