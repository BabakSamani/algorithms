# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(coupons):
    # write your code in Python 3.6
    number_coin = {}
    # First find the repeated numbers
    for i in range(0, len(coupons)):
        # Store repeated number and its index
        if str(coupons[i]) in number_coin:
            number_coin[str(coupons[i])][1] = i
        else:
            number_coin[str(coupons[i])] = [i, -100000]
    print(number_coin)
    # Then find the distance between these repeated numbers to determine the number of coins
    minDistance = 999999
    for s in number_coin:
        print(s)
    # Then select the numbers between the minimum amount of coins
    pass