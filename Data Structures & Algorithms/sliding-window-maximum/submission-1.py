import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k-1

        max_heap = [-digit for digit in nums[left:right+1]]
        heapq.heapify(max_heap)

        removed={k:nums[left:right+1].count(k) for k in nums[left:right+1]}

        result = []
        while right < len(nums):
            
            while True:
                curr_maximum = -max_heap[0] 
                if removed[curr_maximum] <= 0 :
                    heapq.heappop(max_heap)
                else:
                    result.append(curr_maximum)
                    break
            removed[nums[left]]-=1
            
            left +=1
            right +=1

            if right<len(nums):
                removed[nums[right]] = removed.get(nums[right],0)+1
                heapq.heappush(max_heap,-nums[right])

        return result


    

        