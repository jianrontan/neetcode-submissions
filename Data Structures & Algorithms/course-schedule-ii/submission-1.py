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
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            res.append(course)
            prereqs = adj[course]
            for prereq in prereqs:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    queue.append(prereq)
        
        return res if len(res) == numCourses else []