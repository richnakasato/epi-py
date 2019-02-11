from test_framework import generic_test

def calculate(left, right, operator):
    if operator == '+':
        return left + right
    if operator == '-':
        return left - right
    if operator == '*':
        return left * right
    if operator == '/':
        return left / right
    else:
        raise Exception('check operator')


def evaluate(expression):
    # TODO - you fill in here.
    inputs = expression.split(',')
    operands = list()
    operators = ('+', '-', '*', '/')
    for input_ in inputs:
        if input_ not in operators:
            operands.append(int(input_))
        else:
            right = operands.pop()
            left = operands.pop()
            result = calculate(left, right, input_)
            operands.append(int(result))
    return operands[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
