
def complement_exist(comp, num):
    if num in comp:
        return True
    else:
        return False


def main():
    # Desired sum,
    # Should the pairs be one after the other? Not necessarily
    sum = 9

    # Array of numbers that we need to find the pair
    arr = [1, 2, 4, -1, 4, 2, 6, 9, 3, 5, 0, -8, 5, 7, -2, 8, 10, 16]

    pairs = {}

    for i in range(0, len(arr)):
        if arr[i] - sum <= 0:
            k = str(arr[i])
            if not complement_exist(pairs, str(sum-arr[i])):
                pairs[k] = sum - arr[i]
    # Printing out the pair of numbers as key-values dictionary
    print pairs


if __name__ == "__main__":
    main()