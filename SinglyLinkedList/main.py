#!usr/local/bin
from Node import Node
from LinkedList import *


def main():
    linked_list = LinkedList(head=None)

    nodes = [
        Node({'name': "Bob", 'age': 38}),
        Node({'name': "Buddy", 'age': 32}),
        Node({'name': "John", 'age': 35}),
        Node({'name': "Sam", 'age': 23})
    ]

    for i in range(0, len(nodes)):
        linked_list.insert(nodes[i])

    print linked_list.get_size()

    linked_list.publish_all()


if __name__ == '__main__':
    main()
