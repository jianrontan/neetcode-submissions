class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                res.append(asteroid)
            else:
                collision = True
                while collision == True:
                    if len(res) == 0:
                        res.append(asteroid)
                        collision = False
                    elif 0 < res[-1] < abs(asteroid):
                        res.pop()
                    elif 0 < res[-1] > abs(asteroid):
                        collision = False
                    elif 0 < res[-1] == abs(asteroid):
                        res.pop()
                        collision = False
                    else:
                        res.append(asteroid)
                        collision = False
        
        return res