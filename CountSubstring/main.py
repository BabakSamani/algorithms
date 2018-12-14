
def count_substring(string, sub_string):
    m = len(string)
    n = len(sub_string)
    numb_of_matches = 0
    for i in range(0, m - n + 1):
        numb_of_matches += string.count(sub_string, i, i + n)

    return numb_of_matches


if __name__ == "__main__":
    string = raw_input("Enter the string here: ").strip()
    sub_string = raw_input("Enter sub string here: ").strip()
    count = count_substring(string, sub_string)
    print count
