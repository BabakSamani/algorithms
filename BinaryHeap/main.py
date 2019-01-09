#!/usr/bin/python

from BinaryHeap import MinBinaryHeap, MaxBinaryHeap


def main():
    # a_list = [17, 14, 9, 33, 5, 7, 27, 18, 19, 11, 21, 15]
    a_list = [19, 31, 17, 5, 11, 41, 21, 29, 37]
    min_binary_heap = MinBinaryHeap(a_list)
    min_binary_heap.print_heap()

    print("\n")

    max_binary_heap = MaxBinaryHeap(a_list)
    max_binary_heap.print_heap()
    print(max_binary_heap.size)


if __name__ == "__main__":
    main()
