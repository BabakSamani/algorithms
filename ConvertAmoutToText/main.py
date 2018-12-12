#!usr/local/bin
def get_number_string(number):
    num_strings = {'0': "", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven",
                   '8': "eight", '9': "nine", '10': "ten", '20': "twenty", '30': "thirty", '40': "forty",
                   '50': "fifty", '60': "sixty", '70': "seventy", '80': "eighty", '90': "ninety",
                   '100': "hundred", '200': "two hundred", '300': "three hundred", '400': "four hundred",
                   '500': "five hundred", '600': "six hundred", '700': "seven hundred", '800': "eight hundred",
                   '900': "nine hundred", '1000': "thousand"}
    return num_strings.get(number) if num_strings.get(number) else None


def chop_number_left(number, length):
    print (number/pow(10, length-1)) * pow(10, length-1), length
    new_num = number - (number/pow(10, length-1)) * pow(10, length-1)
    if length == 1:
        return number/pow(10, length-1)
    else:
        return chop_number_left(new_num, length-1)


def chop_number_right(number, length):
    new_num = (number - number % 10) / 10
    if number / 10 < 10:
        return new_num
    else:
        print new_num, number % 10
        return chop_number_right(new_num, length - 1)


def main():
    try:
        # chop_number_left(987645, 6)
        # print chop_number_right(98898645, 8)
        user_in = raw_input("Enter the amount: ")
        length = len(user_in)
        number = int(user_in)
        num_str = ''
        while length != 0:
            num = (number/pow(10, length-1)) * pow(10, length-1)
            if num < 10:
                num_str += get_number_string(str(num)) + ' '
            if 10 < num < 100:
                num_str += get_number_string(str(num)) + ' '
            if pow(10, length-1) >= 100:
                num_str += get_number_string(str(number/pow(10, length-1))) + ' '
                num_str += get_number_string(str(pow(10, length-1))) + ' '
            number -= num
            length -= 1
        print num_str
    except ValueError, error:
        print "The amount that you entered is not a number!", error.message


if __name__ == "__main__":
    main()
