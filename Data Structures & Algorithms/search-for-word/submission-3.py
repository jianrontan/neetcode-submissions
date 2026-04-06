class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        self.history = set()
        start = word[0]
        res = False
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == start:
                    res = self.search(i, j, board, word, 0)
                    if res: return True
        return False

    def search(self, i, j, board, word, index):
        res = False
        self.history.add((i, j))
        if index == len(word) - 1:
            return True
        if i - 1 >= 0 and (board[i - 1][j] == word[index + 1]) and (i - 1, j) not in self.history:
            res = self.search(i - 1, j, board, word, index + 1)
        if j - 1 >= 0 and (board[i][j - 1] == word[index + 1]) and (i, j - 1) not in self.history:
            if res == False:
                res = self.search(i, j - 1, board, word, index + 1)
        if i + 1 < len(board) and (board[i + 1][j] == word[index + 1]) and (i + 1, j) not in self.history:
            if res == False:
                res = self.search(i + 1, j, board, word, index + 1)
        if j + 1 < len(board[0]) and (board[i][j + 1] == word[index + 1]) and (i, j + 1) not in self.history:
            if res == False:
                res = self.search(i, j + 1, board, word, index + 1)
        if res == False:
            self.history.remove((i, j))
        return res
