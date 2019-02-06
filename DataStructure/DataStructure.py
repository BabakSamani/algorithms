#!usr/local/bin


class Stack:
    def __init__(self):
        """ Using a python list for implementing the Stack class. """
        self.stack = []
        self.size = 0

    def push(self, data):
        """ A push operation that appends new item on top of the Stack. """
        self.stack.append(data)
        self.size += 1

    def pop(self):
        """ A pop operation that takes out the news item from top of the Stack. """
        if self.size == 0:
            raise Exception("The stack is empty!")
        self.size -= 1
        return self.stack.pop()

    def is_empty(self):
        """ A method that checks whether the stack is empty."""
        return self.size == 0

    def __repr__(self):
        """ Stack representation """
        return "stack: " + str(self.stack)


class Queue:
    def __init__(self):
        """ Using a python list for implementing the Queue class. """
        self.queue = []
        self.size = 0

    def is_empty(self):
        """ A function to see if the queue is empty. """
        return self.size == 0

    def enqueue(self, data):
        """ Adding new element to the queue. """
        self.queue.insert(0, data)
        self.size += 1

    def dequeue(self):
        """ A method for taking out the oldest element form queue. """
        if self.size == 0:
            raise Exception("The queue is empty!")
        self.size -= 1
        return self.queue.pop()

    def __repr__(self):
        """ A method for printing out the queue elements. """
        return "queue: " + str(self.queue)


class CircularBuffer:
    def __init__(self, size):
        """ Constructor of a fixed size buffer. """
        self.buffer = [None] * size
        self.low = 0
        self.high = 0
        self.size = size
        self.count = 0

    def is_empty(self):
        """ A method to see if the buffer is empty."""
        return self.count == 0

    def is_full(self):
        """ A method to check if the buffer is full. """
        return self.count == self.size

    def add(self, data):
        """ A method for adding elements to circular buffer. """
        if self.is_full():
            self.low = (self.low + 1) % self.size
        else:
            self.count += 1
        # Overwrite the value of high index
        self.buffer[self.high] = data
        self.high = (self.high + 1) % self.size

    def remove(self):
        """ A method for removing items from circular buffer."""
        if self.count == 0:
            raise Exception('The circular buffer is empty!')
        value = self.buffer[self.low]
        self.low = (self.low + 1) % self.size
        self.count -= 1
        return value

    def __len__(self):
        """ The len method for having the length of the circular buffer"""
        return self.count

    def __iter__(self):
        """ A python generator that iterates through the circular buffer. """
        index = self.low
        i = self.count
        while i > 0:
            yield self.buffer[index]
            i -= 1
            index = (index + 1) % self.size

    def __repr__(self):
        """ A method for printing out the available elements of the buffer. """
        if self.is_empty():
            return 'circular buffer:[]'

        return 'circular buffer:[' + ','.join(map(str, self)) + ']'


class Node:
    def __init__(self, data, next_node=None):
        """ Constructor for creating a node for linklist. """
        self.data = data
        self.next = next_node


class SinglyLinkList:
    def __init__(self, *start):
        """ Singly Linklist Constructor """
        self.head = None
        self.size = 0

        for _ in start:
            self.prepend(_)

    def prepend(self, data):
        """ Add the data to the beginning of the link list. """
        self.head = Node(data, self.head)
        self.size += 1

    def remove(self, data):
        """ A method for removing an element from the list. """
        h = self.head
        current = None
        while h is not None:
            if h.data == data:
                if current is None:
                    self.head = self.head.next
                else:
                    current.next = h.next
                self.size -= 1
                return True
            current = h
            h = h.next
        return False

    def pop(self):
        """ Remove the first node from the list"""
        if self.head is None:
            raise Exception('The link list is empty!')
        data = self.head.data
        self.head = self.head.next
        return data

    def __iter__(self):
        """ An iterator to iterate trough the link list."""
        h = self.head
        while h is not None:
            yield h.data
            h = h.next

    def __repr__(self):
        """ A method for printing out the available elements of the list.  """
        if self.head is None:
            return 'Link list:[]'
        return 'Link list:[{0:s}]'.format(','.join(map(str, self)))


class QueueLinkList:
    def __init__(self, *start):
        """ The constructor for LinkList type queue."""
        self.head = None
        self.tail = None
        self.size = 0

        for _ in start:
            self.append(_)

    def append(self, data):
        """ Add the data to the beginning of the link list. """
        new_node = Node(data, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def check_infinite(self):
        """ A method to check whether there is an infinite loop in the link list."""
        p1 = p2 = self.head
        while p1 is not None and p2 is not None:
            if p2.next is None:
                return False

            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                return True
        return False

    def pop(self):
        """ Remove the first node from the list"""
        if self.head is None:
            raise Exception('The link list is empty!')
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def __iter__(self):
        """ An iterator to iterate trough the link list."""
        h = self.head
        while h is not None:
            yield h.data
            h = h.next

    def __repr__(self):
        """ A method for printing out the available elements of the list.  """
        if self.head is None:
            return 'Link list:[]'
        return 'Link list:[{0:s}]'.format(','.join(map(str, self)))


class Leaf:
    def __init__(self, data):
        """ A constructor for creating a leaf node for a tree. """
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def compute_height(self):
        """Compute height of node in BST."""
        height = -1
        if self.left:
            height = max(height, self.left.height)
        if self.right:
            height = max(height, self.right.height)

        self.height = height + 1

    def height_difference(self):
        """Compute height difference of node's children in BST."""
        left_target = 0
        right_target = 0

        if self.left:
            left_target = 1 + self.left.height
        if self.right:
            right_target = 1 + self.right.height

        return left_target - right_target

    def rotate_right(self):
        """Perform right rotation around given node."""
        new_root = self.left
        grandson = new_root.right
        self.left = grandson
        new_root.right = self

        self.compute_height()
        return new_root

    def rotate_left(self):
        """Perform left rotation around given node."""
        new_root = self.right
        grandson = new_root.left
        self.right = grandson
        new_root.left = self

        self.compute_height()
        return new_root

    def rotate_left_right(self):
        """Perform left, then right rotation around given node."""
        leaf = self.left
        new_root = leaf.right
        grand1 = new_root.left
        grand2 = new_root.right
        leaf.right = grand1
        self.left = grand2

        new_root.left = leaf
        new_root.right = self

        leaf.compute_height()
        self.compute_height()
        return new_root

    def rotate_right_left(self):
        """Perform right, then left rotation around given node."""
        leaf = self.right
        new_root = leaf.left
        grand1 = new_root.left
        grand2 = new_root.right
        leaf.left = grand2
        self.right = grand1

        new_root.left = self
        new_root.right = leaf

        leaf.compute_height()
        self.compute_height()
        return new_root

    def insert(self, value):
        """Adds a new node to the tree with value and Rebalance as needed."""
        new_root = self

        if value <= self.data:
            self.left = self.__append_to_subtree(self.left, value)
            if self.height_difference() == 2:
                if value <= self.left.value:
                    new_root = self.rotate_right()
                else:
                    new_root = self.rotate_left_right()
        else:
            self.right = self.__append_to_subtree(self.right, value)
            if self.height_difference() == -2:
                if value > self.right.data:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()

        new_root.compute_height()
        return new_root

    @staticmethod
    def __append_to_subtree(root, data):
        if root is None:
            return Leaf(data)
        root = root.insert(data)
        return root

    def find(self, data):
        """ A recursive function for searching on a tree recursively. """
        # Check left side of the tree
        if self.data < data:
            if self.left is None:
                return "\n" + str(data) + " not available on left side of the tree."
            return self.left.find(data)
        # Check right side of the tree
        elif self.data > data:
            if self.right is None:
                return "\n" + str(data) + " not available on right side of the tree."
            return self.right.find(data)
        else:
            return "\n" + str(data) + " is available on the tree."

    def inorder(self):
        """In order traversal generator of tree rooted at given leaf."""
        if self.left:
            for d in self.left.inorder():
                yield d

        yield self.data

        if self.right:
            for d in self.right.inorder():
                yield d

    def remove(self, value):
        """
         Remove value of self from BinaryTree. Works in conjunction with remove
         method in BinaryTree.
        """
        new_root = self

        if self.data == value:
            if self.left is None:
                return self.right

            leaf = self.left
            while leaf.right:
                leaf = leaf.right

            leaf_val = leaf.value
            self.left = self.__remove_from_parent(self.left, leaf_val)
            self.data = leaf_val

            if self.height_difference() == -2:
                if self.right.height_difference() <= 0:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()
        elif self.data > value:
            self.left = self.__remove_from_parent(self.left, value)
            if self.height_difference() == -2:
                if self.right.height_difference() <= 0:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()
        else:
            self.right = self.__remove_from_parent(self.right, value)
            if self.height_difference() == 2:
                if self.left.height_difference() >= 0:
                    new_root = self.rotate_right()
                else:
                    new_root = self.rotate_left_right()

        new_root.compute_height()
        return new_root

    @staticmethod
    def __remove_from_parent(parent, value):
        """Helper method for remove. Ensures proper behavior when removing node that
        has children."""
        if parent:
            return parent.remove(value)
        return None

    def __repr__(self):
        """Useful debugging function to produce linear tree representation."""
        left_sub = ''
        right_sub = ''
        if self.left:
            left_sub = str(self.left)
        if self.right:
            right_sub = str(self.right)
        return "(L:" + left_sub + " " + str(self.data) + " R:" + right_sub + ")"


class BinaryTree:
    def __init__(self):
        self.size = 0
        self.root = None

    def __str__(self):
        if self.root:
            return str(self.root)

    def add(self, value):
        if self.root is None:
            self.root = Leaf(value)
        else:
            self.root.insert(value)
        self.size += 1

    def remove(self, item):
        """
        Remove value from tree.
        """
        if self.root is not None:
            self.root = self.root.remove(item)
            self.size -= 1

    def get_min(self):
        """
        A function for finding the minimum value in the tree
        """
        if self.root is None:
            raise Exception("The binary tree is empty")

        current_root = self.root
        while current_root.left:
            current_root = current_root.left
        return current_root.data

    def get_max(self):
        """
        A method for finding the maximum value in the tree
        """
        if self.root is None:
            raise Exception("The binary tree is empty")

        current_root = self.root
        while current_root.right:
            current_root = current_root.right
        return current_root.data

    def get_closest_value_to(self, target):
        """
        A method for finding the closest value in the tree to the target value
        """
        if self.root is None:
            return None
        leaf = self.root
        best = leaf
        distance = abs(leaf.data - target)

        while leaf is not None:
            if abs(leaf.data - target) < distance:
                best = leaf
                distance = abs(leaf.data - target)

            if target < leaf.data:
                leaf = leaf.left
            elif target > leaf.data:
                leaf = leaf.right
            else:
                return target
        return best.data

    def __contains__(self, data):
        """
        Check whether BST contains target value.
        """
        leaf = self.root
        while leaf is not None:
            if data < leaf.data:
                leaf = leaf.left
            elif data > leaf.data:
                leaf = leaf.right
            else:
                return True
        return False

    def __iter__(self):
        """In-order traversal of elements in the tree."""
        if self.root:
            for e in self.root.inorder():
                yield e

    def __repr__(self):
        if self.root is None:
            return "binary tree:()"
        return "binary tree:" + str(self.root)
