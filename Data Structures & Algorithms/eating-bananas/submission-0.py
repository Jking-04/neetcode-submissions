class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l_bound = 1
        u_bound = max(piles)

        

        while l_bound<=u_bound:
            print(l_bound)
            print(u_bound)

            test = (l_bound+u_bound)//2
            time=0
            for pile in piles:
                time+=(pile+test-1)//test

            if time>h:
                l_bound = test+1
            else:
                u_bound = test-1
        return l_bound

        

       