class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=[]

        for word in strs:
            letters = ''.join(sorted(word))
            
            for group in groups:
                if group[0] == letters:
                    group.append(word)
                    break
            else:
                groups.append([letters,word])
        
        return [group[1:] for group in groups]
        
