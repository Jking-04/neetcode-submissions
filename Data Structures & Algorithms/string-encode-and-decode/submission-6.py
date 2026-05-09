class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in range(len(strs)):
            
            encoded=encoded+str(len(strs[i])) + ":" + strs[i]
            

        
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        words=[]
        str_count = ""
        i=0
        while i < len(s):
            if s[i] != ":":
                str_count +=s[i]
                
            else:
                count = int(str_count)
                temp = i
                i = temp + count
                word = s[temp:i+1]
                words.append(word[1:])
                str_count =""
            i+=1
        return words

            