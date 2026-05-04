class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        searching = {}

        for j in range(len(nums)):
            
            if nums[j] in searching.keys():
                i=searching[nums[j]]
                return [i,j]
            else:
                value = target-nums[j]
                searching[value]=j
        return[0,0]