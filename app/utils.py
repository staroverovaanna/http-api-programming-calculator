class Token:
    def __init__(self, value):
        self.value = value

    def add(self, another_token):
        return self.value + another_token.value

    def subtract(self, another_token):
        return self.value - another_token.value

    def divide(self, another_token):
        try:
            self.value / another_token.value
        except ZeroDivisionError as e:
            # было - Exception
            raise ZeroDivisionError(f'Division by zero: {self.value} / {another_token.value}') from e

        return self.value / another_token.value

    def multiply(self, another_token):
        return self.value * another_token.value

    def calculate(self, another_token, operation):
        if operation.value == '*':
            return self.multiply(another_token)
        if operation.value == '/':
            return self.divide(another_token)
        if operation.value == '+':
            return self.add(another_token)
        if operation.value == '-':
            return self.subtract(another_token)

        else:
            raise Exception(f'Unknown operation {operation.value}')


class Expression:
    # принимает строчку с выражением
    # сначала делит строчку на массив из токенов методом tokenize
    # потом производит вычисления над этим массивом
    # в одном из полей expressionсохранить массив токенов и потом уже его обрабатывать

    def __init__(self, value):
        self.value = value
        self.tokens = self.tokenize()
        self.answer = 0

    def tokenize(self):
        expression = self.value
        # Токенизировать выражение
        tokens = []
        curr_token = ''
        for i, char in enumerate(expression):
            if char.isdigit() or char == '.':
                curr_token += char
            else:
                if curr_token != '':
                    tokens.append(Token(float(curr_token)))
                    curr_token = ''
                if char != ' ':
                    tokens.append(Token(char))
        if curr_token != '':
            tokens.append(Token(float(curr_token)))
        unar_indexes = []
        for i, token in enumerate(tokens):
            if str(token.value) == '-' and (i == 0 or str(tokens[i - 1].value) in "+-*/("):
                tokens[i + 1].value = -1 * tokens[i + 1].value
                unar_indexes.append(i)

        for i in unar_indexes[::-1]:
            tokens.pop(i)

        return tokens

    def calculate(self):
        tokens = self.tokens

        operand_stack = []
        operation_stack = []
        priority = {'+': 1, '-': 1, '*': 2, '/': 2}
        try:
            for i, token in enumerate(tokens):
                # print(token.value)
                if str(token.value) in '+-/*':
                    # если в стаке операций лежит операция с меньшим приоритетом или открыв скобка, кладем в стак наш токен
                    if operation_stack and (operation_stack[-1].value == '(' or priority[operation_stack[-1].value] < priority[token.value]):
                        operation_stack.append(token)

                    # если стак операций пустой - просто складываем нашу операцию в него
                    elif not operation_stack:
                        operation_stack.append(token)

                    # если стак операций непустой и последняя операция с таким же приоритетом и меньше
                    # то выполняем предыдущую операцию в стаке операций для 2 последних операндов в стаке операндов
                    else:
                        while operation_stack and (
                                operation_stack[-1].value != '(' or (
                                priority[operation_stack[-1].value] >= priority[token.value])):
                            operand_2 = operand_stack.pop()
                            operand_1 = operand_stack.pop()
                            operation = operation_stack.pop()
                            res_tmp = Token(operand_1.calculate(operand_2, operation))
                            operand_stack.append(res_tmp)
                        operation_stack.append(token)

                elif token.value == '(':
                    operation_stack.append(token)
                elif token.value == ')':
                    while operation_stack[-1].value != '(':
                        operand_2 = operand_stack.pop()
                        operand_1 = operand_stack.pop()
                        operation = operation_stack.pop()
                        res_tmp = Token(operand_1.calculate(operand_2, operation))
                        operand_stack.append(res_tmp)
                    operation_stack.pop()

                else:
                    operand_stack.append(token)

            # print(operand_stack[-2].value, operation_stack[-1].value, operand_stack[-1].value)
            while operation_stack:
                # print(operand_stack[-2].value, operation_stack[-1].value, operand_stack[-1].value)
                operand_2 = operand_stack.pop()
                operand_1 = operand_stack.pop()
                operation = operation_stack.pop()
                res_tmp = Token(operand_1.calculate(operand_2, operation))
                operand_stack.append(res_tmp)

            # print(operand_stack[0].value)
            return operand_stack[0].value

        except ZeroDivisionError as e:
            raise ZeroDivisionError(f'{e}') from e
