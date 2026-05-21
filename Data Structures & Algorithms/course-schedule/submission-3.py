class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        visited = set()
        for i in range(numCourses):
            path = set()
            def dfs(course):
                if course in visited:
                    return True
                path.add(course)
                for prereq in adj[course]:
                    if prereq in path:
                        return False
                    path.add(prereq)
                    if not dfs(prereq):
                        return False
                path.remove(course)
                visited.add(course)
                return True
            if not dfs(i):
                return False
        
        return True