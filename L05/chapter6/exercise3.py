# Programming exercises chapter 6
# exercise 3

import math
def sphereArea(radius):
   area = 4 * math.pi * radius**2
   return area
def sphereVolume(radius):
    volume = 4/3 * math.pi * radius**3
    return volume
def main():
   r = eval(input("Input a value for the radius: ")) 
   a = sphereArea(r)
   v = sphereVolume(r)
   print("A sphre with radius", r, "has volume", v),"and surface area," a)
main()
