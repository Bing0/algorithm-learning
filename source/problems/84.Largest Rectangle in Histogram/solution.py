class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # height, width
        result = 0
        heights.append(0)

        for height in heights:
            length = 0
            while stack:
                if stack[-1][0] >= height:
                    top_height, top_width = stack.pop()
                    length += top_width
                    result = max(result, top_height * length)
                else:
                    break
            stack.append((height, length + 1))
        return result
