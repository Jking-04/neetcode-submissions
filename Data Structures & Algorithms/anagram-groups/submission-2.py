class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}

        for word in strs:
            letters = ''.join(sorted(word))
            
            if letters in groups:
                groups[letters].append(word)
            else:
                groups[letters] = [word]
        
        return list(groups.values())
        
