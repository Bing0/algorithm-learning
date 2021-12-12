from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        queue = [(0, k)]
        length = [-1] * (n + 1)

        for u, v, w in times:
            edges[u].append((v, w))

        while queue:
            l, v = heappop(queue)
            if length[v] != -1:
                continue
            length[v] = l
            for n_v, w in edges[v]:
                heappush(queue, (l + w, n_v))

        ans = 0
        for i in range(1, n + 1):
            if length[i] == -1:
                return -1
            ans = max(ans, length[i])

        return ans
