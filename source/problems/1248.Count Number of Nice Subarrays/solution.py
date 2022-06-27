from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [0] + nums
        count_dict = {0: 1}
        result = 0

        for i in range(1, len(nums)):
            nums[i] %= 2
            nums[i] += nums[i - 1]
            if nums[i] in count_dict:
                count_dict[nums[i]] += 1
            else:
                count_dict[nums[i]] = 1
            target = nums[i] - k
            if target in count_dict:
                result += count_dict[target]
        return result


# Another similar solution

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        count = [0] * (len(nums) + 1)
        count[0] = 1
        result = 0

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1] % 2

            target = prefix_sum[i] - k
            if target >= 0:
                result += count[target]

            count[prefix_sum[i]] += 1

        return result
