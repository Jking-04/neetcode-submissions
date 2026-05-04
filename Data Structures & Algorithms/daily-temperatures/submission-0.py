class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp_stack = []

        for i in range(len(temperatures)-1,-1,-1):
            while True:
                if not temp_stack or temperatures[i]<temp_stack[-1][0]:
                    if temp_stack:
                        result[i]=temp_stack[-1][1]-i
                    temp_stack.append((temperatures[i],i))
                    break
                else:
                    temp_stack.pop()
            
            
            print(temp_stack)

            
        return result