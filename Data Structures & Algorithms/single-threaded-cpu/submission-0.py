import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)

        heapq.heapify(tasks)
        queued = []
        res = []

        time = 0
        while queued or tasks:
            if not queued:
                process = heapq.heappop(tasks)
                time += process[0] + process[1]
                res.append(process[2])

                while tasks and tasks[0][0] <= time:
                    process = heapq.heappop(tasks)
                    process = [process[1], process[2]]
                    heapq.heappush(queued, process)
            else:
                process = heapq.heappop(queued)
                time += process[0]
                res.append(process[1])

                while tasks and tasks[0][0] <= time:
                    process = heapq.heappop(tasks)
                    process = [process[1], process[2]]
                    heapq.heappush(queued, process)

        return res