#!usr/local/bin
from DoublyLinkedList import DoublyLinkList


def main():
    d_linked_list = DoublyLinkList(head=None, tail=None)

    data = [
        {'name': "Bob", 'age': 38},
        {'name': "Buddy", 'age': 32},
        {'name': "John", 'age': 35},
        {'name': "Sam", 'age': 23}
    ]

    for i in range(0, len(data)):
        d_linked_list.push_to_head(data[i])

    print d_linked_list.get_size()
    d_linked_list.publish()

    d_linked_list.remove_node({'name': "Buddy", 'age': 32})
    print d_linked_list.get_size()
    d_linked_list.publish()

    d_linked_list.append_to_tail({'name': "James", 'age': 22})
    # add a new node here, {'name': "Zack", 'age': 28}, line 32
    d_linked_list.append_to_tail({'name': "Matt", 'age': 35})
    d_linked_list.append_to_tail({'name': "Shane", 'age': 45})
    print d_linked_list.get_size()
    d_linked_list.publish()

    d_linked_list.insert_after(previous_data={'name': "James", 'age': 22}, new_data={'name': "Zack", 'age': 28})
    print d_linked_list.get_size()
    d_linked_list.publish()


if __name__ == '__main__':
    main()
