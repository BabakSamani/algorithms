
def main(number, array_list):
    total = 0
    inserted_str = ''
    result = False
    for item in array_list:
        if total + item > number:
            total -= item
            inserted_str += str(item) + '-'
        if total - item < number:
            total += item
            inserted_str += str(item) + '+'
        if total == number:
            result = True
    print inserted_str
    return result


if __name__ == "__main__":
    print main(2, [1, 4, 3, 2])
