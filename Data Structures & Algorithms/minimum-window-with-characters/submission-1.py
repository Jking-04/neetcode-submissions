class Solution:
    def minWindow(self, s: str, t: str) -> str:
       t_count = {letter:t.count(letter) for letter in t}
       s_count = {}

       left = 0
       right = 0
       best = ""
       while right<len(s):
        
        subword = s[left:right+1]
        s_count = {letter:subword.count(letter) for letter in subword}

        if all(k in s_count and t_count[k]<=s_count[k] for k in t_count.keys() ):

            if best == "" or len(best) > len(subword):
                best = subword

            left+=1
            continue
        
        right += 1

        

       return best