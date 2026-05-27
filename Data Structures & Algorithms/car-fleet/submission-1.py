class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        order = []
        for i in range(len(position)):
            order.append((position[i], speed[i]))
        order.sort(reverse=True)
        
        stack = []
        for position, speed in order:
            time = (target - position) / speed
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)