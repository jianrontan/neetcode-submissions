import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        for source, target, time in times:
            if source not in adjList:
                adjList[source] = []
            adjList[source].append((time, target))
            if target not in adjList:
                adjList[target] = []
        
        res = 0
        visited = [False for _ in range(n)]
        visitCount = 0
        pq = [(0, k)]
        while pq:
            time, node = heapq.heappop(pq)
            if not visited[node - 1]:
                res = max(time, res)
                visited[node - 1] = True
                visitCount += 1
                if visitCount == n:
                    return res
                for item in adjList[node]:
                    heapq.heappush(pq, (item[0] + time, item[1]))
        return -1