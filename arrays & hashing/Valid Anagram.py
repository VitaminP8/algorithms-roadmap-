class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = list(s)
        t_list = list(t)

        if len(s_list) != len(t_list):
            return False
        else:
            for letter in s_list:
                if letter not in t_list:
                    return False
                else:
                    t_list.remove(letter)
        return True

