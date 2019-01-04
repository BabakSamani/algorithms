
# Test case, Sample Input 0
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output 0
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


def main():
    N = int(raw_input())
    myList = []
    for i in range(0, N):
        command = raw_input()
        c = command.split(' ')
        try:
            # insert i e: Insert integer e at position i.
            if c[0] == 'insert':
                myList.insert(int(c[1]), int(c[2]))
            # print: Print the list.
            if c[0] == 'print':
                print myList
            # remove e: Delete the first occurrence of integer e.
            if c[0] == 'remove':
                myList.remove(int(c[1]))
            # append e: Insert integer e at the end of the list.
            if c[0] == 'append':
                myList.append(int(c[1]))
            # sort: Sort the list.
            if c[0] == 'sort':
                myList.sort()
            # pop: Pop the last element from the list.
            if c[0] == 'pop':
                myList.pop()
            # reverse: Reverse the list.
            if c[0] == 'reverse':
                myList.reverse()
        except TypeError as error:
            print "The input is not integer!" + error.message


if __name__ == '__main__':
    main()

# Second test case
# 29
# append 1
# append 6
# append 10
# append 8
# append 9
# append 2
# append 12
# append 7
# append 3
# append 5
# insert 8 66
# insert 1 30
# insert 6 75
# insert 4 44
# insert 9 67
# insert 2 44
# insert 9 21
# insert 8 87
# insert 1 75
# insert 1 48
# print
# reverse
# print
# sort
# print
# append 2
# append 5
# remove 2
# print