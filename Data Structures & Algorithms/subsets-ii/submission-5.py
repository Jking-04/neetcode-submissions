class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        path = []
        self.returns = []

        self.backtrack(0,path)

        return self.returns

    def backtrack(self,start,path):
        self.returns.append(path.copy())

        for i in range(start,len(self.nums)):
            if i>start and self.nums[i] == self.nums[i-1]:
                continue

            path.append(self.nums[i])
            
            self.backtrack(i+1,path)
            path.pop()