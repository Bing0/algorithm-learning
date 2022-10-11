class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        count = len(nums)

        def determine(i, result):
            if i == count:
                ans.append(result[:])
                return
            determine(i + 1, result)
            result.append(nums[i])
            determine(i + 1, result)
            result.pop()

        determine(0, [])
        return ans
