class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.nums = nums

        self.backtrack(0,[])
        return self.results
    
    def backtrack(self,start,path):
        self.results.append(path)

        for i in range(start,len(self.nums)):
            path.append(self.nums[i])
            self.backtrack(i+1,path.copy())
            path.pop()


        