#!usr/local/bin


class Leaf(object):

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_data(self):
        return self.data

    def insert(self, data):
        if self.data:
            # Compare new data with the parent leaf data
            if data < self.data:
                if self.left is None:
                    self.left = Leaf(data)  # Create a new left leaf
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Leaf(data)  # Create a new right leaf
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, data):
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

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()
