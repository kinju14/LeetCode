class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = set()

        while queue:
            pos, speed, steps = queue.popleft()
            if pos == target:
                return steps
            
            if (pos, speed) in visited:
                continue
            
            else:
                visited.add((pos, speed))
                queue.append((pos + speed, speed * 2, steps + 1))

                if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                    speed = -1 if speed > 0 else 1
                    queue.append((pos, speed, steps+1))



