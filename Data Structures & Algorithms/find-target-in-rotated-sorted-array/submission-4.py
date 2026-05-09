class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        left = 0
        right = n-1

        offset = 0

        while left <= right:
            middle = (left+right)//2

            if nums[middle]>nums[n-1]:
                left = middle+1
            else:
                right = middle-1
            
            if middle+1>n-1 or nums[middle]>nums[middle+1]:
                offset = middle+1
                break
    
        left = 0
        right = n-1

        while left <= right:
            middle = (left+right)//2
            offset_middle = (middle+offset)%n

            if nums[offset_middle]<target:
                left = middle+1
            elif  nums[offset_middle]>target:
                right = middle-1
            else:
                return offset_middle
        return -1


        