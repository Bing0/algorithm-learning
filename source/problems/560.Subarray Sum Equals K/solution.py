class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0: 1}
        total = 0
        result = 0

        for index, num in enumerate(nums):
            total += num
            target = total - k
            if target in sum_dict:
                result += sum_dict[target]

            sum_dict[total] = sum_dict.get(total, 0) + 1

        return result
