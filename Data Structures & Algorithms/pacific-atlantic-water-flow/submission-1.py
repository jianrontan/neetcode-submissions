class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic = [[False for _ in range(cols)] for _ in range(rows)]
        
        def findPacific(r, c):
            pacific[r][c] = True
            if r > 0 and heights[r][c] <= heights[r - 1][c] and not pacific[r - 1][c]:
                findPacific(r - 1, c)
            if c > 0 and heights[r][c] <= heights[r][c - 1] and not pacific[r][c - 1]:
                findPacific(r, c - 1)
            if r < rows - 1 and heights[r][c] <= heights[r + 1][c] and not pacific[r + 1][c]:
                findPacific(r + 1, c)
            if c < cols - 1 and heights[r][c] <= heights[r][c + 1] and not pacific[r][c + 1]:
                findPacific(r, c + 1)
        
        def findAtlantic(r, c):
            atlantic[r][c] = True
            if r > 0 and heights[r][c] <= heights[r - 1][c] and not atlantic[r - 1][c]:
                findAtlantic(r - 1, c)
            if c > 0 and heights[r][c] <= heights[r][c - 1] and not atlantic[r][c - 1]:
                findAtlantic(r, c - 1)
            if r < rows - 1 and heights[r][c] <= heights[r + 1][c] and not atlantic[r + 1][c]:
                findAtlantic(r + 1, c)
            if c < cols - 1 and heights[r][c] <= heights[r][c + 1] and not atlantic[r][c + 1]:
                findAtlantic(r, c + 1)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    findPacific(r, c)

        for r in range(rows):
            for c in range(cols):
                if r == rows - 1 or c == cols - 1:
                    findAtlantic(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c]) 

        return res