# Programming exercises chapter 6
# exercise 4

def sumN(n):
    fact = 1
    for factor in range(n,1,-1):
        fact = fact + factor
        return fact
def sumNCubes(n):
    cube = 1
    for factor in range(n,1,-1):
        cube = cube + factor**3
        return cube
def main():
    n = eval(input("Enter a number: "))
    Natural = sumN(n)
    Cubes = sumNCubes(n)
    print("The sum of the first", n, "natural numbers is", Natural)
    print("The sum of the first", n, "numbers cube is", Cubes)
main()
