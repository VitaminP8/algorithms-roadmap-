class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        n2 = len(s2)

        if n > n2:
            return False

        lst = [0] * 26
        for i in range(n):
            lst[ord(s1[i])-ord("a")] += 1

        lst2 = [0]*26
        for i in range(n):
            lst2[ord(s2[i])-ord("a")] += 1
        if lst == lst2[:]:
            return True

        lt = 0
        for i in range(n, n2):
            lst2[ord(s2[i])-ord("a")] += 1
            lst2[ord(s2[lt])-ord("a")] -= 1
            lt += 1
            if lst == lst2[:]:
                return True
        return False
