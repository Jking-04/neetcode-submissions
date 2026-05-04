class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        
        heapq.heapify(heap)
        

        while len(heap)>1:
            current=heapq.heappop(heap)
            second=heapq.heappop(heap)

            current=current-second
            if current!=0:
                heapq.heappush(heap,current)
        if len(heap)==1:
            current=heapq.heappop(heap)

        return -current
        