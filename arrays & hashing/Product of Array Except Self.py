class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        multi = 1
        zero = 0
        ans = [0] * len(nums)

        for num in nums:
            if num == 0:
                zero += 1
            else:
                multi *= num

        if zero > 1:
            return ans
        elif zero == 1:
            for i, num in enumerate(nums):
                if num == 0:
                    ans[i] = multi
                    return ans
        else:
            for i, num in enumerate(nums):
                ans[i] = multi // num
            return ans



class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
