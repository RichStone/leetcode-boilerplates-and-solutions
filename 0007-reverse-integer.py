class Solution:
    def reverse(self, x: int) -> int:
        digits = [digit for digit in str(x)]
        if digits[0] != '-':
            x_positive = True
        else:
            digits.pop(0)
            x_positive = False
        try:
            result = int(''.join(reversed(digits)))
            if not x_positive:
                result *= -1
            if result < 2147483647 and result > -2147483648:
                return result
            else:
                return 0
        except OverflowError:
            return 0


if __name__ == '__main__':
    x = 1534236469
    sol = Solution()
    print('Test Run:')
    print(sol.reverse(x))

