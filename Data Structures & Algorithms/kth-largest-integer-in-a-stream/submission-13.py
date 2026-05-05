class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if self.k>1:
            self.heap = nums
            self.heapify()
            print(self.heap)
            self.check_size()

        else:
            if nums:
                self.curr_max = max(nums)
            else:
                self.curr_max = float("-inf")

    def add(self, val: int) -> int:
        if self.k>1:
            self.heap.append(val)
            i = len(self.heap)-1
            while i>0:
                i = self.sift_up(i)
            print(self.heap)
            self.check_size()

            print(self.heap)
            print("____")

        
            return self.heap[0]
        else:
            self.curr_max = max(self.curr_max,val)
            return self.curr_max

    def heapify(self):
        heap_size = len(self.heap)

        if heap_size >=2:
            for i in reversed(range(heap_size//2)):
                self.sift_down(i)
        

    def sift_down(self,i):
        n = len(self.heap)
        while True:
            left = (i*2)+1
            right = (i*2)+2
            smallest = i

            if left<n and self.heap[smallest]>self.heap[left]:
                smallest = left

            if right<n and self.heap[smallest]>self.heap[right]:
                smallest = right

            if smallest == i:
                break
            
            self.heap[i],self.heap[smallest] = self.heap[smallest],self.heap[i]
            i = smallest

    def sift_up(self,i):
        parent = (i-1)//2

        if self.heap[parent] > self.heap[i]:
            self.heap[i],self.heap[parent] = self.heap[parent],self.heap[i]

            return parent
        else:
            return 0

    def check_size(self):
        while len(self.heap)>self.k:
            self.heap[0] = self.heap[-1]
            self.heap.pop()

            self.sift_down(0)



        


        

    


        
            

        
        
