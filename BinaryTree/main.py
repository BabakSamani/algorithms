from Leaf import Leaf


def main():
    root = Leaf(7)
    root.insert(1)
    root.insert(5)
    root.insert(4)
    root.insert(12)
    root.insert(2)

    root.print_tree()

    print(root.find(13))


if __name__ == "__main__":
    main()
