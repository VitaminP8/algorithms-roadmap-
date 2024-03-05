class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort(key=lambda x: x[0])

        last = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= last:
                last = end
            else:
                result += 1
                last = min(last, end)

        return result