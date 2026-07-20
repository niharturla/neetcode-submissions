class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = sum(len(row) for row in matrix) - 1 # O(1) for lists

        while left <= right:
            mid = left + (right - left) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            #print(row,col)
            element = matrix[row][col]

            if element > target:
                right = mid - 1
            elif element < target:
                left = mid + 1
            else:
                return True
        return False