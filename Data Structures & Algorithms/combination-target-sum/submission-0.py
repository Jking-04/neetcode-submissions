class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.nums = nums
        self.target = target
        path = []
        self.results =[]

        self.backtrack(0,path)
        return self.results
    
    def backtrack(self,start,path):
        if sum(path) == self.target:
            self.results.append(path)

        for i in range(start,len(self.nums)):
            path.append(self.nums[i])

            if sum(path) <= self.target:
                self.backtrack(i,path.copy())
            path.pop()

        