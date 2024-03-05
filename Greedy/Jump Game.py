class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0

        for num in nums:
            if jump < 0:
                return False
            elif jump < num:
                jump = num
            jump -= 1

        return True