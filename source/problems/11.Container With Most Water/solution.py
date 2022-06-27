class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        result = 0

        while i < j:
            if height[i] < height[j]:
                result = max(result, (j - i) * height[i])
                i += 1
            else:
                result = max(result, (j - i) * height[j])
                j -= 1
        return result