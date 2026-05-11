class Solution:
    def minWindow(self, s: str, t: str) -> str:
       t_count = {letter:t.count(letter) for letter in t}
       s_count = {}

       left = 0
       old_right = -1
       right = 0
       best = ""
       while right<len(s) and left<len(s):
        
        if right != old_right:
            if s[right] not in s_count:
                s_count[s[right]] = 1
            else:
                s_count[s[right]] += 1
        old_right = right

        if all(k in s_count and t_count[k]<=s_count[k] for k in t_count.keys() ):
            subword = s[left:right+1]
            if best == "" or len(best) > len(subword):
                best = subword

            s_count[s[left]]-=1
            left+=1
            continue
        
        right += 1

       return best