class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        temp = 0
        word_set = set()
        start = 0

        for i in range(len(s)):
            while s[i] in word_set:
                word_set.remove(s[start])
                start += 1

            word_set.add(s[i])
            temp = i - start + 1
            max_length = max(max_length, temp)

        return max_length
