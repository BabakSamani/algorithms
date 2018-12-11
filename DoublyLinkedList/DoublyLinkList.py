#!usr/local/bin
from Node import Node


class DoublyLinkList(object):
    # class constructor
    def __init__(self, head=None):
        self.head = head
        self.size = 0
