import unittest


def insert_minus_plus(number, array_list):
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


class UnitTest(unittest.TestCase):
    def insert_test(self):
        self.assertTrue(insert_minus_plus(2, [1, 4, 3, 2]), True)
        self.assertTrue(insert_minus_plus(10, [1, 4, 3, 2]), True)


if __name__ == "__main__":
    print insert_minus_plus(2, [1, 4, 3, 2])
    unittest.main()
