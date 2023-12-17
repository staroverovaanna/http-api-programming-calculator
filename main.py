

def tokenize(expression):
    # Токенизировать выражение
    tokens = []
    curr_token = ''
    for i, char in enumerate(expression):
        if char.isdigit() or char == '.':
            curr_token += char
        else:
            if curr_token != '':
                tokens.append(float(curr_token))
                curr_token = ''
            if char != ' ':
                tokens.append(char)
    if curr_token != '':
        tokens.append(float(curr_token))
    unar_indexes = []
    for i, token in enumerate(tokens):
        if token == '-' and (i == 0 or tokens[i - 1] in "+-*/("):
            tokens[i + 1] = -1 * tokens[i + 1]
            unar_indexes.append(i)

    for i in unar_indexes[::-1]:
        tokens.pop(i)

    return tokens


def calc_two_numbers(operand_1, operand_2, operation):
    if operation == '*':
        return operand_1 * operand_2
    if operation == '/':
        if operand_2 == 0:
            try:
                operand_1 / operand_2
            except ZeroDivisionError as e:
                raise Exception('Division by zero!') from e
        return operand_1 / operand_2
    if operation == '+':
        return operand_1 + operand_2
    if operation == '-':
        return operand_1 - operand_2


def calcalate(tokens):
    # print(tokens)
    operand_stack = []
    operation_stack = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    for i, token in enumerate(tokens):
        print(token)
        if str(token) in '+-/*':
            # если в стаке операций лежит операция с меньшим приоритетом или открыв скобка, кладем в стак наш токен

            if operation_stack and (operation_stack[-1] == '(' or priority[operation_stack[-1]] < priority[token]):
                operation_stack.append(token)
            # если стак операций пустой - просто складываем нашу операцию в него
            elif not operation_stack:
                operation_stack.append(token)

            # если стак непустой и последняя операция с таким же приоритетом
            # то выполняем предыдущую операцию в стаке операций для 2 последних операндов в стаке операндов
            else:
                while operation_stack and (operation_stack[-1] != '(' or (priority[operation_stack[-1]] >= priority[token])):
                    operand_2 = operand_stack.pop()
                    operand_1 = operand_stack.pop()
                    operation = operation_stack.pop()
                    res_tmp = calc_two_numbers(operand_1, operand_2, operation)
                    operand_stack.append(res_tmp)
                operation_stack.append(token)

        elif token == '(':
            operation_stack.append(token)
        elif token == ')':
            while operation_stack[-1] != '(':
                operand_2 = operand_stack.pop()
                operand_1 = operand_stack.pop()
                operation = operation_stack.pop()
                res_tmp = calc_two_numbers(operand_1, operand_2, operation)
                operand_stack.append(res_tmp)
            operation_stack.pop()

        else:
            operand_stack.append(token)

    while operation_stack:
        operand_2 = operand_stack.pop()
        operand_1 = operand_stack.pop()
        operation = operation_stack.pop()
        res_tmp = calc_two_numbers(operand_1, operand_2, operation)
        operand_stack.append(res_tmp)

    return operand_stack[0]

# expression = "-2 * (3 + 4) - 5 / 2"
# tokens = tokenize(expression)
#
# print(calcalate(tokens))