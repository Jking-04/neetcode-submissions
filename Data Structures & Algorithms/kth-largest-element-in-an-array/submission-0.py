class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = nums
        self.heapify()

        for i in range(k):
            largest = self.heap[0]
            if len(self.heap) > 1:
                self.heap[0] = self.heap.pop()
                self.siftDown(0)
        return largest

    def heapify(self):
        n = len(self.heap)
        for i in reversed(range(n//2)):
            self.siftDown(i)
    
    def siftDown(self,i):
        n = len(self.heap)
        while True:
            left = (i*2) + 1
            right = (i*2) + 2
            largest = i

            if left<n and self.heap[largest] < self.heap[left]:
                largest = left
            
            if right<n and self.heap[largest] < self.heap[right]:
                largest = right

            if largest == i:
                break

            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]

            i = largest



        