#!usr/local/bin
import random


def main():
    n = 1000
    # Create random array of n numbers with randomly distributed order
    rand_nums = random.sample(range(1, n+1), n)
    # Generate a random index
    rand_index = random.sample(range(0, n), 1)
    rand_index = rand_index[0]

    # Now set the number in that index to zero
    rand_nums[rand_index] = 0
    total = 0
    for i in range(0, n):
        total += rand_nums[i]

    missing = n * (n + 1)/2 - total
    return missing


if __name__ == '__main__':
    print(main())
