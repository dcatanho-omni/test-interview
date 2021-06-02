import sys

ROMAN_THOUSANDS = ('', 'M', 'MM', 'MMM')
ROMAN_HUNDREDS = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
ROMAN_TENS = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
ROMAN_ONES = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', "IX")


def digits(number):
    number_digits = []

    for i in range(3, 0, -1):
        value = number // 10 ** i
        number_digits.append(value)
        number = number - value * (10 ** i)

    number_digits.append(number)
    return number_digits


def to_roman(number):
    roman_digits = digits(number)
    roman_number = ROMAN_THOUSANDS[roman_digits[0]] + ROMAN_HUNDREDS[roman_digits[1]] + \
        ROMAN_TENS[roman_digits[2]] + ROMAN_ONES[roman_digits[3]]
    return roman_number


def main():
    print("To exit hit Ctrl-d")

    while True:
        try:
            numeral = int(input("> "))
            if numeral < 1 or numeral > 4000:
                print("Please, write a number between 1 and 4000")
            else:
                print("Your number is: {0}".format(to_roman(numeral)))
        except EOFError:
            print("Good bye!")
            sys.exit()


if __name__ == '__main__':
    main()
