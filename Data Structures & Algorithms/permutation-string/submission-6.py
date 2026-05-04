class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count={}
        window_count={}

        left = 0

        for c in s1:
            s1_count[c]=s1_count.get(c,0)+1

        for right in range(len(s2)):
            window_count[s2[right]]=window_count.get(s2[right],0)+1

            if right - left + 1 > len(s1):
                window_count[s2[left]]-=1

                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]

                left+=1

            if s1_count == window_count:
                return True

        return False
                
