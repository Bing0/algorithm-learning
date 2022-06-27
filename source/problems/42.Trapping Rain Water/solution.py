# Solution 1. Use two pointer
class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0

        while height[i] == 0 and i < j:
            i += 1
        while height[j] == 0 and i < j:
            j -= 1

        min_height = min(height[i], height[j])
        while i < j:
            if height[i] <= height[j]:
                if min_height > height[i]:
                    res += min_height - height[i]
                else:
                    min_height = height[i]
                i += 1
            else:
                if min_height > height[j]:
                    res += min_height - height[j]
                else:
                    min_height = height[j]
                j -= 1

        return res

# Solution 2. Use stack.

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # (width, height)
        result = 0

        for h in height:
            length = 1
            while stack:
                if h > stack[-1][1]:
                    min_h = min(stack[0][1], h)
                    lw, lh = stack.pop()
                    result += lw * (min_h - lh)
                    length += lw
                else:
                    break
            stack.append((length, h))
        return result