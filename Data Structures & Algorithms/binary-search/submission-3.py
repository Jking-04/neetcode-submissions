class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L_ptr=0
        R_ptr=len(nums)-1

        while L_ptr<=R_ptr:
            mid_ptr =(L_ptr+R_ptr)//2
            val = nums[mid_ptr]

            if val>target:
                R_ptr=mid_ptr-1
            if val<target:
                L_ptr=mid_ptr+1
            if val==target:
                return mid_ptr
        return -1 