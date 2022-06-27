class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            visited = set()
            result = []
            for num in nums:
                to_find = target - num
                if to_find in visited:
                    result.append([num, to_find])
                visited.add(num)

            return result

        visited = set()
        founded = set()
        result = []
        for index, num in enumerate(nums):
            if num not in visited:
                twos = twoSum(nums[index + 1:], -num)
                visited.add(num)
                for two in twos:
                    tmp = [num] + two
                    found = tuple(sorted(tmp))
                    if found not in founded:
                        result.append(tmp)
                        founded.add(found)
        return result
