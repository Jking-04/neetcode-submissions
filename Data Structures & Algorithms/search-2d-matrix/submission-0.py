class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m  = len(matrix[0])-1
        n = len(matrix)-1

        left_row = 0
        left_col=0

        right_row = n
        right_col = m

        left = (left_col + left_row * (m+1))
        right = (right_col + right_row * (m+1))

        while left <= right:
            middle = (left + right)//2
            
            middle_col = middle%(m+1)
            middle_row = middle//(m+1)

            print(f"{middle_col}/{middle_row}")

            if matrix[middle_row][middle_col]==target:
                return True
            elif matrix[middle_row][middle_col] < target:
                left = middle +1
            else:
                right = middle - 1
        return False