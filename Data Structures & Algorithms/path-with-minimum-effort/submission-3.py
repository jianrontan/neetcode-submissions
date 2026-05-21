import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]] # [diff, row, col]
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while minHeap:
            node = heapq.heappop(minHeap)
            diff, row, col = node[0], node[1], node[2]

            if row == ROWS - 1 and col == COLS - 1:
                return diff

            if (row, col) in visited:
                continue

            visited.add((row, col))
            height = heights[row][col]

            for r, c in directions:
                if row + r >= 0 and row + r < ROWS and col + c >= 0 and col + c < COLS and (row + r, col + c) not in visited:
                    nextHeight = heights[row + r][col + c]
                    heapq.heappush(minHeap, [max(diff, abs(nextHeight - height)), row + r, col + c])