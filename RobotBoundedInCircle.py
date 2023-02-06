class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = (1, 0)
        pos = (0, 0)
        for ins in instructions:
            if ins == 'G':
                pos = (pos[0] + direction[0], pos[1] + direction[1])
            elif ins == 'L':
                direction = (-direction[1], direction[0])
            elif ins == 'R':
                direction = (direction[1], -direction[0])
        return pos == (0, 0) or direction != (1, 0)
