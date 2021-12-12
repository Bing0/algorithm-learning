from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += c
            if digits[i] == 10:
                c = 1
                digits[i] = 0
            else:
                c = 0
                break
        if c == 1:
            digits.insert(0, 1)
        return digits