# mini boiler


if __name__ == '__main__':
    print('Test Run:')

# boiler with one input


if __name__ == '__main__':
    # sample input
    inputs = [ ]

    # solution init
    sol = Solution()

    print('Test Run:')
    for input in inputs:
        print('#############')
        print('sample input: ' + str(input))
        output = sol.isPalindrome(input)
        print('output: ' + output)
        print('#############')

# CONCURRENCY BOILER

from threading import Thread, Condition


def printNumber(num):
    print(num, end='')


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        printNumber(0)

    def even(self, printNumber: 'Callable[[int], None]') -> None:

        printNumber(2)

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        printNumber(1)


if __name__ == '__main__':
    instance = ZeroEvenOdd(3)
    A = Thread(target=instance.zero, args=(printNumber,))
    B = Thread(target=instance.even, args=(printNumber,))
    C = Thread(target=instance.odd, args=(printNumber,))
    A.run()
    C.run()
