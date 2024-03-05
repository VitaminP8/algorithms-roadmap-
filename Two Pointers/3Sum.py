class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        sum = 0
        ans = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if i == len(nums)-1 or nums[i] > 0:
                break
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    if [nums[i], nums[l], nums[r]] not in ans:
                        ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

        return ans


