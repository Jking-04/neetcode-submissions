class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_count={}
        left = 0
        best=0
        max_freq = 0

        for right in range(len(s)):
            letter_count[s[right]] = letter_count.get(s[right],0)+1
            max_freq = max(max_freq, letter_count[s[right]])

            print(letter_count)

            while(right - left + 1) - max_freq >k:
                letter_count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


                

                
                




        