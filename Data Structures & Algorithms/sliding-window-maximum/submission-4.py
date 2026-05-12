import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k-1

        max_heap = [(-digit,index) for index,digit in enumerate(nums[left:right+1])]
        heapq.heapify(max_heap)

        result = []
        while right < len(nums):
            
            while True:
                curr_maximum = max_heap[0] 
                if curr_maximum[1] < left:
                    heapq.heappop(max_heap)
                else:
                    result.append(-curr_maximum[0])
                    break
            
            left +=1
            right +=1

            if right<len(nums):
                heapq.heappush(max_heap,(-nums[right],right))

        return result


    

        