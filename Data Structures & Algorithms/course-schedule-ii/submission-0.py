from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        indegrees = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            indegrees[b] += 1
            adj[a].append(b)
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
        
        if len(res) == numCourses:
            res.reverse()
            return res
        else:
            return []