from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        n = len(grid)

        dist = {0: 1}
        queue = deque([0])

        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        target = n * n - 1

        while queue:
            first = queue.popleft()
            if first == target:
                return dist[first]

            x = first // n
            y = first % n

            for x_o, y_o in offsets:
                x_n = x + x_o
                y_n = y + y_o
                if x_n < 0 or y_n < 0 or x_n >= n or y_n >= n:
                    continue
                if grid[x_n][y_n] == 1:
                    continue
                index = x_n * n + y_n
                if index in dist:
                    continue
                dist[index] = dist[first] + 1
                queue.append(index)

        return -1
