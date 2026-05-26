class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        order = []
        for i in range(len(position)):
            order.append((position[i], speed[i]))
        order.sort(reverse=True)
        
        fleets = 0
        max_time = 0
        for position, speed in order:
            time = (target - position) / speed
            if max_time < time:
                max_time = time
                fleets += 1

        return fleets