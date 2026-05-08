class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.string = s
        self.result = []

        self.backtrack(0,[])
        return self.result

    def backtrack(self,start,path):
        if start == len(self.string):
            self.result.append(path.copy())
        for i in range(start,len(self.string)):
            new_string = self.string[start:i+1]
            if new_string == new_string[::-1]:
                path.append(new_string)
                self.backtrack(i+1,path)
                path.pop()
            else:
                continue
            


        
        