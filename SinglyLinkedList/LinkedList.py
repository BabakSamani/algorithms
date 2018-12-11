#!usr/local/bin


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.size = 0

    def insert(self, new_node):
        try:
            new_node.set_next(self.head)
            self.head = new_node
            self.size += 1
            return True
        except Exception as error:
            print(error.message)

    def get_size(self):
        return self.size

    def search(self, node):
        data = node.get_data()
        current_node = self.head
        found = False
        while current_node and found is False:
            if current_node.data == data:
                found = True
            else:
                current_node = current_node.get_next()

        if current_node is None:
            raise ValueError("Data is not in the list")
        return current_node

    def delete(self, node):
        data = node.get_data()
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

    def publish_node(self, node):
        if self.size != 0:
            try:
                current_node = self.head
                found = False
                counter = 1
                while current_node is not None and found is False:
                    if current_node.get_data() == node.get_data():
                        found = True
                    else:
                        current_node = current_node.get_next()
                        counter += 1
                if found:
                    print 'This node is found in ', counter + 1, ' place.'
                if not found:
                    print 'This node is not exist in the list'
            except Exception as error:
                print(error.message)

    def publish_all(self):
        if self.size != 0:
            try:
                current_node = self.head
                while current_node is not None:
                    print(current_node.get_data())
                    current_node = current_node.get_next()
            except Exception as error:
                print(error.message)
        else:
            print "There is nothing to publish!"
