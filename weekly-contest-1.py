class Solution:
    def getNoZeroIntegers(self, n: int):
        for i in range(1, n, 1):
            complement = n - i
            if '0' not in str(i) and '0' not in str(complement):
                return [i, complement]

    def minFlips(self, a: int, b: int, c: int) -> int:
        if a + b == c:
            return 0
        print(format(a, 'b'))
        print(format(b, 'b'))
        print(format(c, 'b'))


if __name__ == '__main__':
    # sample input
    # inputs = [2, 11,10000,69, 1010]
    inputs = [[2, 6, 5], [4, 2, 7], [1, 2, 3]]

    # solution init
    sol = Solution()

    print('Test Run:')
    for input in inputs:
        print('#############')
        print('sample input: ' + str(input))
        output = sol.minFlips(input[0], input[1], input[2])
        # output = sol.getNoZeroIntegers(input)
        print('output: ' + str(output))
        print('#############')