
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i, j = m - 1, n - 1
        k = len(nums1) - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]



# [1,2,3,4,0,0]
# [5,6]


# [6,7,8,8,0,0,0,0]
# [1,2,3,8]