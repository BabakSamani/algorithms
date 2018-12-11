#!usr/local/bin
from Node import Node


class DoublyLinkList(object):
    # class constructor
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def push_to_head(self, new_data):
        # Create a new node from new data
        new_node = Node(new_data)

        # Set next and previous nodes for new node
        new_node.set_next_node(self.head)
        new_node.set_previous_node(None)

        # Change previous node of the head node to new node
        if self.head is not None:
            self.head.set_previous_node(new_node)

        # change the head pointer to the new node
        self.head = new_node
        self.size += 1

    def insert_after(self, previous_data, new_data):
        # Create the previous node from previous data
        previous_node = Node(previous_data)
        # Create new node from new data
        new_node = Node(new_data)
        # Check if previous data is available
        if previous_node.get_data() is None:
            print "The previous node does not exist"
            return
        else:
            # Get the position of desired previous node
            current_node = self.head
            while current_node and current_node.get_data() != previous_data:
                # Current node indicates the position of the previous node
                current_node = current_node.get_next_node()

            if current_node.get_next_node() is not None:
                new_node.set_next_node(current_node.get_next_node())
                new_node.set_previous_node(current_node)

                current_node.set_next_node(new_node)
                next_curr_node = current_node.get_next_node()
                next_curr_node.set_previous_node(new_data)

                self.size += 1
            else:
                print 'It seems you are trying to add this new node to the tail. Use "append_to_tail" function instead.'

    def append_to_tail(self, new_data):
        new_node = Node(new_data)
        end = self.head

        new_node.set_next_node(None)

        if self.head is None:
            new_node.set_previous_node(None)
            self.head = new_node
            return

        while end.get_next_node() is not None:
            end = end.get_next_node()

        end.set_next_node(new_node)
        new_node.set_previous_node(end)

        self.size += 1

    def remove_node(self, data):
        current_node = self.head
        previous_node = None

        while current_node and current_node.get_data() != data:
            previous_node = current_node
            current_node = current_node.get_next_node()

        if previous_node is None:
            self.head = current_node.get_next_node()
        elif current_node:
            previous_node.set_next_node(current_node.get_next_node())
            current_node.set_next_node(None)
        self.size -= 1

    def find_node(self, data):
        node = Node(data)
        data = node.get_data()
        current_node = self.head
        found = False
        while current_node and found is False:
            if current_node.data == data:
                found = True
            else:
                current_node = current_node.get_next_node()

        if current_node is None:
            raise ValueError("Data is not in the list")
        return current_node

    def get_size(self):
        return self.size

    def publish(self):
        if self.size != 0:
            try:
                current_node = self.head
                while current_node is not None:
                    print(current_node.get_data())
                    current_node = current_node.get_next_node()
            except Exception as error:
                print(error.message)
        else:
            print "There is nothing to publish!"
