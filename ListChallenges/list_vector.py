#!usr/local/bin


def compare(a, b):
    return (a > b) - (a < b)


def main():
    made = ["Ford", "Honda", "Toyota", "Nissan", "Dodge", "Hyundai", "Audi", "Kia", "Volvo"]
    for index, item in enumerate(made):
        print(index, "->", item)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sum(nums))

    toyota = ["Yaris", "Mirai",  "Camry", "Avalon", "Prius", "Corolla"]
    i = iter(toyota)

    count = 0
    while count < len(toyota):
        print(i.__next__())  # in python 3.* and in python 2 is i.next())
        count += 1

    s = ", ".join(toyota)
    print(s)

    toyota_sorted_list = sorted(toyota)
    print(toyota_sorted_list)

    print(compare("Mirai", "Camry"))

    toyota.sort()
    print(toyota)
    # print(toyota.pop())

    toyota.reverse()
    print(toyota)

    # Using list as a stack
    stack = [3, 4, 6]
    stack.append(8)
    stack.append(7)
    stack.append(5)
    stack.append(9)
    print(stack)
    stack.pop()
    print(stack)

    # Using list as a queue
    stack.clear()
    stack.insert(0, 2)
    print(stack)
    stack.insert(0, 4)
    print(stack)
    stack.insert(0, 6)
    print(stack)
    stack.insert(0, 3)
    print(stack)
    stack.insert(0, 5)
    print(stack)
    stack.insert(0, 8)
    print(stack)
    first_num = stack.pop()
    print("First inserted number: ", first_num)
    print(stack)

    squares = list(map(lambda x: x ** 2, range(10)))
    print(squares)


if __name__ == "__main__":
    main()
