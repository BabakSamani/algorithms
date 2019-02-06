#!usr/local/bin
from DataStructure import Stack, Queue, CircularBuffer, QueueLinkList, BinaryTree


def main():
    s = Stack()
    s.push(1)
    s.push(4)
    s.push(5)
    print(s)

    q = Queue()
    q.enqueue(1)
    q.enqueue(4)
    q.enqueue(0)
    print(q)

    cb = CircularBuffer(5)
    cb.add(2)
    cb.add(8)
    cb.add(5)
    cb.add(12)
    # cb.add(7)
    # print(cb)
    # cb.add(3)
    print(cb)
    # print(cb.is_full())
    # print(len(cb))

    qll = QueueLinkList()
    qll.append(1)
    qll.append(2)
    qll.append(3)
    qll.append(4)

    qll.pop()
    print(qll)
    # print(qll.check_infinite())

    bt = BinaryTree()
    bt.add(1)
    # print("Root: ", bt.root.data)
    bt.add(7)
    # print("Right leaf: ", bt.root.right.data)
    bt.add(2)
    # print("Left leaf: ", bt.root.left.data)
    bt.add(4)
    # print("Left left leaf: ", bt.root.left.left.data)
    bt.add(3)
    # print("Left right leaf: ", bt.root.left.right.data)
    bt.add(9)
    # bt.add(20)
    bt.add(0)

    # bt.remove(20)

    print(bt)

    for _ in bt:
        print(_)
    # print(bt.size)
    # print(3 in bt)
    # print(bt.get_max())
    # print(bt.get_min())


if __name__ == "__main__":
    main()
