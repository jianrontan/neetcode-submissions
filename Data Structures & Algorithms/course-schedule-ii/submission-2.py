from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            indegrees[a] += 1
            adj[b].append(a)
        res = []

        queue = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            res.append(course)
            for prereq in adj[course]:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    queue.append(prereq)
        
        return res if len(res) == numCourses else []