class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = points
        for i in range(len(self.heap)):
            self.heap[i] = (calcDistance(self.heap[i]),self.heap[i])

        self.heapify()

        results = []
        for _ in range(k):
            _,curr_min_point = self.heap[0]
            results.append(curr_min_point)
            if len(self.heap)>1:
                self.heap[0] = self.heap.pop()
                self.siftDown(0)
            else:
                break

        return results

    def heapify(self):
        n = len(self.heap)
        for i in reversed(range(n//2)):
            self.siftDown(i)

    def siftDown(self,i):
        n = len(self.heap)
        while True:
            left = (i*2) + 1
            right = (i*2)+2
            smallest = i

            if left<n and self.heap[left][0]<self.heap[smallest][0]:
                smallest = left
            
            if right<n and self.heap[right][0]<self.heap[smallest][0]:
                smallest = right

            if smallest == i:
                break
            
            self.heap[i],self.heap[smallest] = self.heap[smallest],self.heap[i]

            i = smallest

def calcDistance(point):
    x,y = point
    dist = ((x**2) + (y**2))**0.5
    return dist
        