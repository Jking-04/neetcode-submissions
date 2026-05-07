class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = [[]]
        curr_path = []
        self.find_results(nums,curr_path)
        return self.results
    
    def find_results(self,nums,curr):
        if nums:
            for i,next_candidate in enumerate(nums):
                new_sub_set = curr.copy()
                new_sub_set.append(next_candidate)
                if set(new_sub_set) not in [set(sub_set) for sub_set in self.results]: 
                    self.results.append(new_sub_set)
        
                    self.find_results(nums[:i] + nums[i+1:],new_sub_set)



        