from threading import Thread, Condition, enumerate


def printNumber(num):
    print(num, end='')


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.zeros_turn = True
        self.condition = Condition()

    def is_zeros_turn(self):
        return self.zeros_turn

    def is_even_turn(self):
        return not self.zeros_turn and self.count % 2 == 0

    def is_odd_turn(self):
        return not self.zeros_turn and self.count % 2 != 0


    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            try:
                if self.count < self.n:
                    raise Exception('terminate B')
            except:
                print('no more evens needed')
            with self.condition:
                self.condition.wait_for(self.is_zeros_turn)
                printNumber(0)
                if self.count == 0:
                    self.count += 1
                self.zeros_turn = False
                self.condition.notify_all()
                print(enumerate())

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            try:
                if self.n - self.count < 2:
                    raise Exception('terminate B')
            except:
                print('no more evens needed')
            with self.condition:
                self.condition.wait_for(self.is_even_turn)
                printNumber(self.count)
                self.count += 1
                self.zeros_turn = True
                self.condition.notify_all()
                print(enumerate())


    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:

            with self.condition:
                self.condition.wait_for(self.is_odd_turn)
                printNumber(self.count)
                self.count += 1
                self.zeros_turn = True
                self.condition.notify_all()
                print(enumerate())


if __name__ == '__main__':
    instance = ZeroEvenOdd(2)
    A = Thread(target=instance.zero, args=(printNumber,), name='A')
    B = Thread(target=instance.even, args=(printNumber,), name='B')
    C = Thread(target=instance.odd, args=(printNumber,), name='C')
    A.start()
    B.start()
    C.start()
