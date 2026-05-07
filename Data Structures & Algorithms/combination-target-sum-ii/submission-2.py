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
        
        visited_values = set()
        
        for i in range(start,len(self.candidates)):

            if self.candidates[i] in visited_values:
                continue

            path.append(self.candidates[i])
            visited_values.add(self.candidates[i])

            if sum(path)<=self.target:
                self.backtrack(i+1,path.copy())
            
            path.pop()
        