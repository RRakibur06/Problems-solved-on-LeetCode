class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        temp = [row[:] for row in matrix]
        x = len(matrix) - 1
        
        for r in range(len(temp)):
            for c in range(len(temp[r])):
                matrix[c][x] = temp[r][c]
            x -= 1