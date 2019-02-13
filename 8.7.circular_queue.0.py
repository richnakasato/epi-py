from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self.queue = [None] * capacity
        self.growth = 2
        self.sz = 0
        self.head = 0
        self.tail = 0
        return

    def enqueue(self, x):
        # TODO - you fill in here.
        if self.sz == len(self.queue):
            temp = [None] * (self.growth * len(self.queue))
            temp_idx = 0
            curr_idx = self.head
            for times in range(self.sz):
                temp[temp_idx] = self.queue[curr_idx]
                temp_idx += 1
                curr_idx = (curr_idx + 1) % len(self.queue)
            self.queue = temp
            self.head = 0
            self.tail = self.sz
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % len(self.queue)
        self.sz += 1
        return

    def dequeue(self):
        # TODO - you fill in here.
        if not self.sz:
            raise Exception('empty queue')
        temp = self.queue[self.head]
        self.head = (self.head + 1) % len(self.queue)
        self.sz -= 1
        return temp

    def size(self):
        # TODO - you fill in here.
        return self.sz


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
