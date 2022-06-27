class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = digits[:]
        c = 1
        for index, digit in reversed(list(enumerate(digits))):
            digit += c
            c = int(digit / 10)
            digit = digit % 10
            result[index] = digit
        if c:
            result = [c] + result

        return result