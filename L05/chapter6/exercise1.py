# Programming exercises chapter 6
# exercise 1
# A program for the lyrics of OldMacDonald

def oldMac():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

def animal(animal, sound):
   print("And on his farm he had a", animal, "Ee-igh, Ee-igh, Oh!") 
   print("With a", sound,",", sound, "here and a", sound, ",", sound, "there.")
   print("Here a ", sound, ",", "there a", sound, ", everywhere a", sound, ",", sound)

def main():
    oldMac()
    animal("cow", "moo")
    oldMac()
    print()
    oldMac()
    animal("sheep", "bäh")
    oldMac()
    print()
    oldMac()
    animal("chicken", "piep")
    oldMac()
    print()
    oldMac()
    animal("horse", "neigh")
    oldMac()
    print()
    oldMac()
    animal("dog", "wuff")
    oldMac()
    print()
main()

