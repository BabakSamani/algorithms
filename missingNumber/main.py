#!usr/local/bin
import random


def main():
    # Create random array with randomly distributed numbers
    # return np.random.randint(1, 101, 100)
    rand_index = random.sample(range(0, 100), 1)
    rand_index = rand_index[0]
    rand_nums = random.sample(range(1, 101), 100)
    print rand_nums[rand_index]
    return sorted(rand_nums, key=int)


if __name__ == '__main__':
    print main()
