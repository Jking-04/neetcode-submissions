class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = sorted(s)
        t_letters = sorted(t)

        if s_letters == t_letters:
            return True
        else:
            return False