class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]

        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(curSum, maxSum)

        return maxSum
