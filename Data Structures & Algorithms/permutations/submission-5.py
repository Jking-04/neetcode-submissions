class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        path = []
        self.result = []

        self.backtrack(path)

        return self.result

    def backtrack(self,path):
        if len(path) == len(self.nums):
            self.result.append(path.copy())
        else:

            for number in self.nums:
                if number in path:
                    continue

                path.append(number)
                self.backtrack(path)
                path.pop()
        