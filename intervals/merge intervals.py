class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        i = 1
        intervals.sort(key=lambda x: x[0])

        if len(intervals) == 1:
            return intervals

        while i < len(intervals):
            if intervals[i - 1][1] < intervals[i][0]:
                result.append(intervals[i - 1])
                i += 1
            elif intervals[i - 1][1] >= intervals[i][0]:
                while i < len(intervals) and intervals[i - 1][1] >= intervals[i][0]:
                    intervals[i][0] = min(intervals[i - 1][0], intervals[i][0])
                    intervals[i][1] = max(intervals[i - 1][1], intervals[i][1])
                    i += 1

        result.append(intervals[i-1])
        return result
