class Solution:
    def minWindow(self, s: str, t: str) -> str:
       if t == "":
        return ""
       t_count = {letter:t.count(letter) for letter in t}
       s_count = {}

       left = 0
       old_right = -1
       right = 0
       best = ""

       total = len(t_count)
       formed = 0

       while right<len(s) and left<len(s):
        
        if right != old_right:
            if s[right] not in s_count:
                s_count[s[right]] = 1
            else:
                s_count[s[right]] += 1

            if s[right] in t_count:
                if s_count[s[right]] == t_count[s[right]]:
                    formed += 1
        old_right = right

       

        if formed == total:
            subword = s[left:right+1]
            if best == "" or len(best) > len(subword):
                best = subword

            s_count[s[left]]-=1

            if s[left] in t_count:
                if s_count[s[left]] < t_count[s[left]]:
                    formed -=1

            left+=1
            continue
        
        right += 1

       return best