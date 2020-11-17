# Programming exercises chapter 11
# Exercise 7

def innerProdukt(list1, list2):
    product = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            product.append(list1[i] * list2[i])
        return product
    else: 
        return False
def main():
    list1 = [1,2,3,4,5,6]
    list2 = [7,8,9,4,2,3]

    print("the inner Produkt is:", innerProdukt(list1,list2))
main()