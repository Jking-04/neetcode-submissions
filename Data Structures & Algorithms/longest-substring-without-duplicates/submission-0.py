class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        count = {}
        max_length = 0

        while right<len(s):
            count[s[right]] = count.get(s[right],0) + 1
            
            while count[s[right]] > 1:
                count[s[left]] -=1
                left += 1
            
            right += 1
            max_length = max(max_length, right - left)
        
        return max_length
        