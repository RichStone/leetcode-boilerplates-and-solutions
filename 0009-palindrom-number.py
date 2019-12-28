class Solution:
    def isPalindrome(self, x: int) -> bool:
        if len(str(x)) == 1:
            return True
        if x < 0:
            return False
        nums = [digit for digit in str(x)]
        nums_to_check = round(len(nums) / 2)
        for i in range(nums_to_check):
            # special cases
            if nums[i] != nums[-i - 1]:
                print(nums[i])
                print(nums[-i - 1])
                return False
        return True


if __name__ == '__main__':
    # sample input
    inputs = [121, -121, 10, 3344, 5665, 12345, 12321]

    # solution init
    sol = Solution()

    print('Test Run:')
    for input in inputs:
        print('input ' + str(input))
        output = sol.isPalindrome(input)
        print(output)