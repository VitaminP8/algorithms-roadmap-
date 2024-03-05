class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            TotalTime = 0
            for banana in piles:
                if banana % k == 0:
                    TotalTime += (banana // k)
                else:
                    TotalTime += ((banana // k) + 1)
            if TotalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res