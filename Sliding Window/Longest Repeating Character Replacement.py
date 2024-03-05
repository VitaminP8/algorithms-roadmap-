class Solution:
    def characterReplacement(self, s, k):
        counts = {}
        max_frequence = 0
        l = 0
        for r, ch in enumerate(s):
            counts[ch] = 1 + counts.get(ch, 0)
            max_frequence = max(max_frequence, counts[ch])
            if max_frequence + k < r - l + 1:
                counts[s[l]] -= 1
                l += 1

        return len(s) - l