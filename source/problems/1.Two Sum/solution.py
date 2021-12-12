class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for index in range(len(nums)):
            to_find = target - nums[index]
            if to_find in visited:
                return [index, visited[to_find]]
            else:
                visited[nums[index]] = index