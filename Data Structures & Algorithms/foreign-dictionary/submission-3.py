from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        deg = {}
        count = 0
        
        for i in range(1, len(words)):
            prev = words[i - 1]
            word = words[i]
            ite = min(len(word), len(prev))
            
            for k in range(len(prev)):
                if prev[k] not in adj:
                    adj[prev[k]] = []
                    count += 1
                if prev[k] not in deg:
                    deg[prev[k]] = 0
            
            processed = False
            for j in range(ite):
                if word[j] == prev[j]:
                    continue
                processed = True
                if prev[j] not in adj:
                    adj[prev[j]] = []
                    count += 1
                if word[j] not in adj:
                    adj[word[j]] = []
                    count += 1
                adj[prev[j]].append(word[j])
                if prev[j] not in deg:
                    deg[prev[j]] = 0
                if word[j] not in deg:
                    deg[word[j]] = 0
                deg[word[j]] += 1
                break
            if processed == False and len(prev) > len(word):
                return ""
            
        for k in range(len(words[-1])):
            word = words[-1]
            if word[k] not in adj:
                adj[word[k]] = []
                count += 1
            if word[k] not in deg:
                deg[word[k]] = 0
        
        head = words[0][0]
        queue = deque()
        for key in adj.keys():
            if deg[key] == 0:
                queue.append(key)
        processed = 0
        res = ""
        while queue:
            cur = queue.popleft()
            processed += 1
            res += cur
            if cur in adj:
                for char in adj[cur]:
                    deg[char] -= 1
                    if deg[char] == 0:
                        queue.append(char)
        
        if processed == count:
            return res
        return ""