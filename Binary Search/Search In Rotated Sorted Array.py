class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[l] < nums[r] or nums[l] <= target or nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < target:
                if nums[l] < nums[r] or nums[r] >= target or nums[mid] > nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1