# Solution one. If the prefix is negative, it is useless. A negative value plus another num is less than num.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        result = -10e5

        for num in nums:
            if prefix_sum <= 0:
                prefix_sum = num
            else:
                prefix_sum += num
            result = max(result, prefix_sum)

        return result


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        min_total = total
        result = total
        for num in nums[1:]:
            total += num
            if total - min_total > result:
                result = total - min_total
            if total < min_total:
                min_total = total
        return result