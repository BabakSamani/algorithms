# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, K):
    # write your code in Python 3.6
    result = ''
    temp = ''
    t = 0
    for i in range(len(S) - 1, -1, -1):
        # Filtering out the dash character
        if S[i].isalnum():
            # Count for number of characters, K
            if t != K:
                temp += S[i].upper()
                t += 1
            else:
                t = 0
                temp += '-' + S[i].upper()

    for t in range(len(temp) - 1, -1, -1):
        result += temp[t]
    return result
    pass


if __name__ == "__main__":
    print solution('2-4A0r7-4k', 4)
    print solution('2-4A0r7-4k', 3)
    print solution('2-4A0r7-4k', 2)
    print solution('r', 1)
