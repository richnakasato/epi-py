from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def empty(self):
        # TODO - you fill in here.
        return not self.s1

    def max(self):
        # TODO - you fill in here.
        if not self.s1:
            raise Exception('empty stack!')
        return self.s2[-1]

    def pop(self):
        # TODO - you fill in here.
        if not self.s1:
            raise Exception('empty stack!')
        temp = self.s1.pop()
        if temp == self.s2[-1]:
            self.s2.pop()
        return temp

    def push(self, x):
        # TODO - you fill in here.
        self.s1.append(x)
        if not self.s2 or x >= self.s2[-1]:
            self.s2.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
