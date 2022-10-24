import sys


def return_digits(number):
    """
    (str) -> str
    Return number that user has printed in 7 lines.
    >>> return_digits('28')
    ' 222  888 \\n2   28   8\\n2  2 8   8\\n  2   888 \\n\
 2   8   8\\n2    8   8\\n22222 888 '
    """

    Zero = ["  ***  ",
            " *   * ",
            "*     *",
            "*     *",
            "*     *",
            " *   * ",
            "  ***  "]

    One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
    Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
    Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
    Four = ["   *  ", "  **  ", " * *  ",
            "*  *  ", "******", "   *  ", "   *  "]
    Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
    Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
    Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
    Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
    Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
    Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

    try:
        digits = number
        row = 0
        output = ''
        while row < 7:
            line = ""
            column = 0
            while column < len(digits):
                number = int(digits[column])
                digit = Digits[number]
                line += digit[row].replace('*', f'{number}')
                column += 1
            if row == 6:
                output += line
            else:
                output += line+'\n'
            row += 1
        return output
    except ValueError as err:
        print(err, "in", digits)


# print(return_digits(41072819))
# number_list = list(number)
# total = []
# for i in range(len(number_list)):
#     total.append(digits[i])
# print(total)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod(verbose=True))
    # try:
    #     digits = sys.argv[1]
    #     print(return_digits(digits))
    # except IndexError:
    #     print("usage: bigdigits.py <number>")
