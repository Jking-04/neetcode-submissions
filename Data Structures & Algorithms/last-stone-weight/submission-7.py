class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = list(map(lambda x: -x,stones))
        
        heapq.heapify(heap)
        

        while len(heap)>1:
            current=heapq.heappop(heap)
            second=heapq.heappop(heap)

            current=current-second

            heapq.heappush(heap,current)
            second=0
        if len(heap)==1:
            current=heapq.heappop(heap)

        return -current
        