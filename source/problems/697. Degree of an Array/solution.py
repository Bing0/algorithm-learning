class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        position_dict = {}
        degree_dict = {}
        max_degree = 0
        min_length = len(nums)

        for index, num in enumerate(nums):
            if num in position_dict:
                length = index - position_dict[num] + 1
                degree = degree_dict[num] + 1
            else:
                position_dict[num] = index
                length = 1
                degree = 1

            degree_dict[num] = degree

            if degree > max_degree:
                min_length = length
                max_degree = degree
            elif degree == max_degree:
                min_length = min(min_length, length)

        return min_length