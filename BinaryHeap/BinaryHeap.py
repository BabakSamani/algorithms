#!/usr/bin/python
# Source: https://medium.com/maxkimambo/binary-heap-implementation-in-python-491afec205

class MaxBinaryHeap:
    def __init__(self, _leaves):
        if not isinstance(_leaves, list):
            raise TypeError('Please enter initial list of leaves')
        self.leaves = _leaves
        # create empty list to store our heap
        self.heap = []
        self.size = 0
        for leaf in _leaves:
            self.add_leaf(leaf)
            self.size += 1

    def add_leaf(self, leaf):
        index = self.size
        self.heap.insert(index, leaf)
        self.heapify_up()

    def remove_root(self):
        result = self.heap.pop(0)
        self.heapify_down()
        return result

    def heapify_up(self, leaf_to_insert=0):
        print("Heapifying up ...")
        if leaf_to_insert == 0:
            current_leaf = self.heap.index(self.heap[-1])  # leaf being percolated
        else:
            current_leaf = leaf_to_insert

        print(f"Current leaf : {current_leaf}")

        # if its the first element we don't need to percolate
        if len(self.heap) == 1:
            print("Nothing for heapifying up")
            return

        print("Heapifying ...")
        # Using integer division would be the same as (x-1)/2 which allows us to find the root
        root_index = (current_leaf // 2)
        root_value = self.heap[root_index]

        if self.heap[current_leaf] > root_value:
            print("Swapping ...")

            # do the swap
            tmp_root = self.heap[root_index]
            self.heap[root_index] = self.heap[current_leaf]
            self.heap[current_leaf] = tmp_root
            # current leaf takes index of the root
            current_leaf = root_index
            # swap complete
            print(f"Swapped {current_leaf} to position of {self.heap[root_index]}")
            return self.heapify_up(current_leaf)

    def heapify_down(self, leaf_to_insert=0):
        print("Heapifying down ...")
        current_leaf = leaf_to_insert

        print(f"Current leaf {current_leaf}")

        if not current_leaf:
            last_leaf = self.heap.pop()
            # Move last leaf to be the root
            self.heap = [last_leaf] + self.heap

        root, leaf_index = self.max_leaf(current_leaf)

        print(f"Leaf {root} , leaf index: {leaf_index}")
        if not root or not leaf_index:
            return

        # check if swap is necessary
        if root >= self.heap[current_leaf]:
            # do the swap
            tmp = self.heap[current_leaf]
            self.heap[current_leaf] = self.heap[leaf_index]
            self.heap[leaf_index] = tmp
            # swap complete
            print(f"Swapped {self.heap[leaf_index]} to position of {self.heap[current_leaf]}")

            # continue percolating at the child level
            return self.heapify_down(leaf_index)

    def max_leaf(self, leaf_index):

        left_leaf_index = (2 * leaf_index) + 1
        right_leaf_index = (2 * leaf_index) + 2

        try:
            left_child = self.heap[left_leaf_index]
            right_child = self.heap[right_leaf_index]

            root = max(left_child, right_child)
            if left_child == root:
                return root, left_leaf_index

            if right_child == root:
                return root, right_leaf_index

        except IndexError:
            # means there are no leaves for this root
            return None, None

    def print_heap(self):
        print(f"{self.heap}")


class MinBinaryHeap:
    def __init__(self, _leaves):
        if not isinstance(_leaves, list):
            raise TypeError('Please enter initial list of leaves')
        self.leaves = _leaves
        # create empty list to store our heap
        self.heap = []
        self.size = 0
        for leaf in _leaves:
            self.add_leaf(leaf)
            self.size += 1

    def add_leaf(self, leaf):
        index = self.size
        self.heap.insert(index, leaf)
        self.heapify_down()

    def remove_root(self):
        result = self.heap.pop(0)
        self.heapify_up()
        return result

    def heapify_up(self, leaf_to_insert=0):
        print("Heapifying up ...")
        if leaf_to_insert == 0:
            current_leaf = self.heap.index(self.heap[-1])  # leaf being percolated
        else:
            current_leaf = leaf_to_insert

        print(f"Current leaf : {current_leaf}")

        # if its the first element we don't need to percolate
        if len(self.heap) == 1:
            print("Nothing for heapifying up")
            return

        print("Heapifying ...")
        # Using integer division would be the same as (x-1)/2 which allows us to find the root
        root_index = (current_leaf // 2)
        root_value = self.heap[root_index]

        if self.heap[current_leaf] < root_value:
            print("Swapping ...")
            # do the swap
            tmp_root = self.heap[root_index]
            self.heap[root_index] = self.heap[current_leaf]
            self.heap[current_leaf] = tmp_root
            # current leaf takes index of the root
            current_leaf = root_index
            # swap complete
            print(f"Swapped {current_leaf} to position of {self.heap[root_index]}")
            return self.heapify_up(current_leaf)

    def heapify_down(self, leaf_to_insert=0):
        print("Heapifying down ...")
        current_leaf = leaf_to_insert

        print(f"Current leaf {current_leaf}")

        if not current_leaf:
            last_leaf = self.heap.pop()
            # Move last leaf to be the root
            self.heap = [last_leaf] + self.heap

        root, leaf_index = self.min_leaf(current_leaf)

        print(f"Leaf {root} , leaf index: {leaf_index}")
        if not root or not leaf_index:
            return

        # check if swap is necessary
        if root <= self.heap[current_leaf]:
            # do the swap
            tmp = self.heap[current_leaf]
            self.heap[current_leaf] = self.heap[leaf_index]
            self.heap[leaf_index] = tmp
            # swap complete
            print(f"Swapped {self.heap[leaf_index]} to position of {self.heap[current_leaf]}")

            # continue percolating at the child level
            return self.heapify_down(leaf_index)

    def min_leaf(self, leaf_index):

        left_leaf_index = (2 * leaf_index) + 1
        right_leaf_index = (2 * leaf_index) + 2

        try:
            left_child = self.heap[left_leaf_index]
            right_child = self.heap[right_leaf_index]

            root = min(left_child, right_child)
            if left_child == root:
                return root, left_leaf_index

            if right_child == root:
                return root, right_leaf_index

        except IndexError:
            # means there are no leaves for this root
            return None, None

    def print_heap(self):
        print(f"{self.heap}")