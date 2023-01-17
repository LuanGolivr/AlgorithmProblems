class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        for i in range(len(matrix)):
            left = 0
            right = len(matrix[0]) - 1

            if target <= matrix[i][-1]:
                while left <= right:
                    m = (left + right) // 2

                    if matrix[i][m] == target:
                        return True
                    
                    elif matrix[i][m] < target:
                        left += 1
                    else:
                        right -= 1
        
        return False
    
    #TC = O(log(N * M))
    #SC = O(1)
