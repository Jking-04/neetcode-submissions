class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        text = "()"
        self.n = n-1
        self.result = []

        self.backtrack(text,start = 0,depth = 0)
        return self.result
    
    def backtrack(self,text,start,depth):
        if depth == self.n:
            self.result.append(text)
            return

        for i in range(start,len(text)):
            new_text = text[:i] + "()" + text[i:]
            self.backtrack(new_text,i+1,depth+1)

