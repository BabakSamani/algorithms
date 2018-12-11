class Node(object):
    # class constructor
    def __init__(self, data=None, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_previous_node(self):
        return self.previous_node

    def set_previous_node(self, previous_node):
        self.previous_node = previous_node