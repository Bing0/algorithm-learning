from typing import List
from collections import defaultdict
from sys import maxsize


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        length = [maxsize] * (n + 1)

        length[k] = 0
        for _ in range(n):
            updated = False

            for u, v, w in times:
                if length[u] == maxsize:
                    continue
                if length[v] > length[u] + w:
                    length[v] = length[u] + w
                    updated = True
            if not updated:
                break

        ans = 0
        for i in range(1, n + 1):
            ans = max(ans, length[i])

        if ans == maxsize:
            return -1
        return ans
