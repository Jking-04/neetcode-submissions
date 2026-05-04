class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        solutions = []

        for i in range(len(nums)-2):
            if (i>0) and (nums[i] == nums[i-1]):
                continue
            j=i+1
            k=len(nums)-1

            target = 0 - nums[i] 

            while(j<k):
                summed_j_k = nums[j]+nums[k]
                if summed_j_k < target:
                    j+=1
                elif summed_j_k > target:
                    k-=1
                else:
                    triplet=[nums[i],nums[j],nums[k]]
                    solutions.append(triplet)
                    
                    j+=1
                    k-=1
                    
                    while (j<k) and (nums[j]==nums[j-1]):
                        j+=1
                    while (j<k) and (nums[k]==nums[k+1]):
                        k-=1

        return solutions
