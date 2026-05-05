
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = stones
        self.heapify()

        while len(self.heap)>2:
            print(self.heap)
            stone_A = self.heap[0]
            self.heap[0]=self.heap.pop()
            self.siftDown(0)

            print(self.heap)
            stone_B = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.siftDown(0)

            new_stone = stone_A - stone_B
            self.heap.append(new_stone)
            self.siftUp(len(self.heap)-1)

            print(len(self.heap))
        
        if len(self.heap)==2:
            return max(self.heap)-min(self.heap)
        else:
            return self.heap[0]

    def heapify(self):
        n = len(self.heap)

        for i in reversed(range(n//2)):
            self.siftDown(i)

    
    def siftDown(self,i):
        n = len(self.heap)
        while True:
            left = (i*2)+1
            right = (i*2)+2
            largest = i

            if left<n and self.heap[largest]<self.heap[left]:
                largest = left
            
            if right<n and self.heap[largest]<self.heap[right]:
                largest = right

            if largest == i:
                break
            
            self.heap[largest],self.heap[i] = self.heap[i],self.heap[largest]
            i = largest
    
    def siftUp(self,i):
        while i !=0:
            parent = (i-1)//2

            if self.heap[parent]<self.heap[i]:
                self.heap[parent],self.heap[i] = self.heap[i],self.heap[parent]
            else:
                break
            i = parent






        