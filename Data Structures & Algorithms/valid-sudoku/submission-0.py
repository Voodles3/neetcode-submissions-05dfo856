class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen_in_row = set()
            for num in row:
                if num in seen_in_row:
                    return False
                if num != ".":
                    seen_in_row.add(num)
        for i in range(9):
            seen_in_column = set()
            for row in board:
                num = row[i]
                if num in seen_in_column:
                    return False
                if num != ".":
                    seen_in_column.add(num)
        squares = {}
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                square = (i // 3) * 3 + (j // 3)
                nums = squares.get(square, set())
                if num in nums:
                    return False
                if num != ".":
                    nums.add(num)
                    squares[square] = nums
        return True
        
