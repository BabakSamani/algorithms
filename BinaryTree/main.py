from Leaf import Leaf


def main():
    # root = Leaf(7)
    # root.insert(1)
    # root.insert(5)
    # root.insert(4)
    # root.insert(12)
    # root.insert(2)
    #
    # root.print_tree()
    #
    # print(root.find(13))

    a_list = [1, 4, 3, 2]
    root = Leaf(a_list[0])
    left_val = a_list[0]
    right_val = a_list[0]

    for l in range(1, len(a_list)-1):
        left_val -= a_list[l]
        right_val += a_list[l]

        root.insert(left_val)
        root.insert(right_val)

    root.print_tree()


if __name__ == "__main__":
    main()
