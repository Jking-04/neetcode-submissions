import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        self.counts = dict(Counter(tasks))
        self.wait_q = dict()

        self.heap = [[-v,k] for k,v in self.counts.items()]
        heapq.heapify(self.heap)

        min_time = 0
        while self.heap or self.wait_q:
            
            if self.heap:
                current_task = heapq.heappop(self.heap)

                self.counts[current_task[1]] -=1
                if self.counts[current_task[1]]>0:
                    self.wait_q[current_task[1]] = n+1

            ended_wait = []
            for task in self.wait_q:
                self.wait_q[task] -= 1
                if self.wait_q[task] ==0 and self.counts[task]>0:
                    heapq.heappush(self.heap,[-self.counts[task],task])
                    self.wait_q[task] = -1
                    ended_wait.append(task)
            
            for task in ended_wait:
                del(self.wait_q[task])

            min_time +=1
            
        return min_time

        