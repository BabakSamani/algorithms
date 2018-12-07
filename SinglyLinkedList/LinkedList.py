#!usr/local/bin
from Node import Node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, data):
        try:
            new_node = Node(data)
            new_node.set_next(self.head)
            self.head = new_node
            self.size += 1
            return True
        except Exception as error:
            print(error.message)

    def get_size(self):
        return self.size

    def search(self, data):
        current_node = self.head
        found = False
        while current_node and found is False:
            if current_node.data == data:
                found = True
            else:
                current_node = current_node.get_next()

        if current_node is None:
            raise ValueError("Data not in list")
        return current_node

    def delete(self, data):
        try:
            current_node = self.head
            previous_node = None
            found = False
            while current_node and found is False:
                if current_node.data == data:
                    found = True
                else:
                    previous_node = current_node
                    current_node = current_node.get_next()
            if current_node is None:
                raise ValueError("Data not in list")
            if previous_node is None:
                self.head = current_node.get_next()
            else:
                previous_node.set_next(current_node.get_next())
                self.size -= 1
                return True
        except Exception as error:
            print(error.message)
            return False

    def publish(self):
        if self.size != 0:
            try:
                current_node = self.head
                while current_node is not None:
                    print(current_node.get_data())
                    current_node = current_node.get_next()
            except Exception as error:
                print(error.message)
        else:
            print("There is nothing to publish!")