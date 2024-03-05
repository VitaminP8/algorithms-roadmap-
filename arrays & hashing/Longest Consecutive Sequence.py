class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n-1) not in numSet:
                long = 1
                while (n+long) in numSet:
                    long += 1
                longest = max(long, longest)
        return longest