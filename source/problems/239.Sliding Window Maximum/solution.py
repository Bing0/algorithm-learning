
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()  # (index, num)
        result = []
        for index, num in enumerate(nums):
            while queue:
                if queue[0][0] <= index - k:
                    queue.popleft()
                else:
                    break
            while queue:
                if queue[-1][1] < num:
                    queue.pop()
                else:
                    break
            queue.append((index, num))
            result.append(queue[0][1])
        return result[k-1:]