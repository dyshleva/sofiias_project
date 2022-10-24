def calculate_expression(expression):
    '''
    (str) -> int
    Find which function wants user to do with printed numbers. if action is not "додати"/"плюс",
    "відняти"/"мінус", "помножити на", "поділити на" and does not start with  «Скільки буде»
    return «Неправильний вираз!».

    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 2?')
    'Неправильний вираз!'
    '''
    if isinstance(expression, str) is not True:
        return

    if expression.startswith("Скільки буде "):
        expression = expression[13:]
    else:
        return 'Неправильний вираз!'

    if expression.endswith('?'):
        expression = expression[:-1]

    list_1 = expression.split()

    numbers = []
    number_index = []
    diya = []
    global final
    for i in range(len(list_1)):
        if list_1[i].isnumeric() or list_1[i].lstrip('-').isdigit():
            numbers.append(list_1[i])
            number_index.append(i)
            if i != (len(list_1)-1):
                if isinstance(list_1[i+1], str) is not True:
                    final = 'Неправильний вираз!'
                    return final
        else:
            diya.append(list_1[i])

    for i in range(len(diya)):
        if diya[i] == 'на':
            diya[i-1] = diya[i-1]+' на'
    if 'на' in diya:
        diya.remove('на')
    if len(diya) == 0:
        final = 'Неправильний вираз!'

    def diyaty1(index_diya):
        global final
        if diya_znachennya == 'відняти' or diya_znachennya == 'мінус':
            final = int(numbers[index_diya])-int(numbers[index_diya+1])
        elif diya_znachennya == 'додати' or diya_znachennya == 'плюс':
            final = int(numbers[index_diya])+int(numbers[index_diya+1])
        elif diya_znachennya == 'помножити на':
            final = int(numbers[index_diya])*int(numbers[index_diya+1])
        elif diya_znachennya == 'поділити на':
            final = int(numbers[index_diya])/int(numbers[index_diya+1])
        else:
            final = 'Неправильний вираз!'

    def diyaty(index_diya):
        global final

        if diya_znachennya == 'відняти' or diya_znachennya == 'мінус':
            final = int(final-int(numbers[index_diya+1]))
        elif diya_znachennya == 'додати' or diya_znachennya == 'плюс':
            final = int(final+int(numbers[index_diya+1]))
        elif diya_znachennya == 'помножити на':
            final = int(final*int(numbers[index_diya+1]))
        elif diya_znachennya == 'поділити на':
            final = int(final/int(numbers[index_diya+1]))
        else:
            final = 'Неправильний вираз!'

    for index_diya, diya_znachennya in enumerate(diya):
        if len(diya) == 0:
            final = 'Неправильний вираз!'

        elif index_diya == 0:
            diyaty1(index_diya)

        elif index_diya != 0 and final != 'Неправильний вираз!':
            diyaty(index_diya)
    return final


if __name__ == "__main__":
    import doctest
    print(doctest.testmod(verbose=True))
