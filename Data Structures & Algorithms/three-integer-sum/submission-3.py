class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        solutions = []

        for i in range(len(nums)-1):
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
                    if triplet not in solutions:
                        solutions.append(triplet)
                    
                    j+=1
                    k-=1
        return solutions
