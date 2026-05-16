class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect = 0
        
        stack_left_max = []
        best_1 = []

        for i,bar in enumerate(heights):
            while stack_left_max and bar <= stack_left_max[-1][0]:
                stack_left_max.pop()

            if stack_left_max:
                best_1.append(stack_left_max[-1][1])
            else:
                best_1.append(-1)

            stack_left_max.append((bar,i))

        stack_right_max = []
        best_2 = []

        for i, bar in reversed(list(enumerate(heights))):
            while stack_right_max and bar <= stack_right_max[-1][0]:
                stack_right_max.pop()

            if stack_right_max:
                best_2.append(stack_right_max[-1][1])
            else:
                best_2.append(len(heights))
                        
            stack_right_max.append((bar,i))
        best_2.reverse()

        for i,bar in enumerate(heights):
            size = bar * (best_2[i]-best_1[i]-1)
            max_rect = max(max_rect,size)

        return max_rect

        