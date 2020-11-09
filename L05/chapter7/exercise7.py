# Programming exercises chapter 7 
# exercise 7
# A Program to calculate the price of a babysitter

def time(time_str):
    hour_str, min_str = time_str.split(":")
    hour = int(hour_str)
    minute = int(min_str)
    return hour + minute / 60

def main():
    start_str = input("Enter the starting time: ")
    start = time(start_str)
    end_str = input("Enter the end time: ")
    end = time(end_str)

    before9 = 2.5
    after9 = 1.75

    if end < 21:
        cost = (end - start) * before9
    elif start < 21 and end >= 21:
        cost = (21-start) * before9 + (end-21) *after9
    else:
        cost = (end - start) * after9
    print("The babysitting price cost is: ", cost)
main()