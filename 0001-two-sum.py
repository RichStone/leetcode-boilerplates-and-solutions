class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        if target > 0:
            nums = [num for num in nums if num < target]
        if target < 0:
            nums = [num for num in nums if num > target]
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                next_index = i + j + 1
                if num1 + num2 == target:
                    return [i, next_index]


if __name__ == '__main__':
    print('Test Run:')
