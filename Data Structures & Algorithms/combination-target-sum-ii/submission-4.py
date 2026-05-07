class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.target = target

        path = []
        self.result = []

        self.backtrack(0,path)

        
        return self.result

    def backtrack(self,start,path):
        if sum(path) == self.target:
            self.result.append(path)
        
        for i in range(start,len(self.candidates)):

            if i > start and self.candidates[i] == self.candidates[i - 1]:
                continue

            path.append(self.candidates[i])

            if sum(path)<=self.target:
                self.backtrack(i+1,path.copy())
            
            path.pop()
        