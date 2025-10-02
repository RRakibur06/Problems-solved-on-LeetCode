class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]

                if cell == '.':
                    continue

                box_index = (i // 3) * 3 + j // 3

                if (cell in rows[i] or 
                    cell in cols[j] or 
                    cell in boxes[box_index]):
                    return False

                rows[i].add(cell)
                cols[j].add(cell)
                boxes[box_index].add(cell)

        return True