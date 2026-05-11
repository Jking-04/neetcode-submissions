class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]*len(height)
        right_max = [0]*len(height)

        curr_max = 0
        for i,value in enumerate(height):
            curr_max = max(curr_max,value)
            left_max[i] = curr_max

        curr_max = 0
        for i,value in enumerate(reversed(height)):
            curr_max = max(curr_max,value)
            right_max[i] = curr_max
        right_max.reverse()
        
        total = 0
        for i in range(len(height)):
            total += (min(left_max[i],right_max[i]))-height[i]

        print(left_max)
        print(right_max)

        return total
        