#!usr/local/bin
import math
import random
from AVG import AVG


def main():
    numbers = [1, 4, 2, 5, 3, 6, 8, 9, 7, 10]

    n = 900
    # Create random array of n numbers with randomly distributed order
    numbers = random.sample(range(1, n+1), n)

    size = len(numbers)

    BottomFive = int(math.ceil(0.05 * size))
    TopFive = int(math.floor(0.95 * size))

    print(BottomFive, TopFive)

    avg = AVG()
    for i in range(BottomFive, TopFive):
        avg.update_sum(numbers[i])
        avg.update_size()

    print(avg.calculate_avg())


if __name__ == "__main__":
    main()
