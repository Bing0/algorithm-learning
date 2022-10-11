class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set()
        result = 0
        for item in obstacles:
            obs.add((item[0], item[1]))

        # N: 0, E: 1, S: 2, W: 3
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir = 0

        x, y = (0, 0)

        for command in commands:
            if command == -1:
                dir = (dir + 1) % 4
            elif command == -2:
                dir = (dir + 3) % 4
            else:
                for i in range(command):
                    x_n = x + dirs[dir][0]
                    y_n = y + dirs[dir][1]

                    if (x_n, y_n) in obs:
                        break
                    x, y = (x_n, y_n)

                result = max(result, x * x + y * y)
        return result