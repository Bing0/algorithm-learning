from typing import List
# Solution 1. Move one step each time.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            to_check = numbers[i] + numbers[j]
            if to_check == target:
                return [i + 1, j + 1]
            elif to_check < target:
                i += 1
            else:
                j -= 1


# Solution 2. Try to skip more position.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            value = numbers[i] + numbers[j]
            if value == target:
                return [i + 1, j + 1]

            if value > target:
                find = target - numbers[i]
                x = i + 1
                y = j
                while x <= y:
                    mid = int((x + y) / 2)
                    if numbers[mid] == find:
                        return [i + 1, mid + 1]
                    if numbers[mid] > find:
                        y = mid - 1
                    else:
                        x = mid + 1
                j = y
            else:
                find = target - numbers[j]
                x = i
                y = j - 1
                while x <= y:
                    mid = int((x + y) / 2)
                    if numbers[mid] == find:
                        return [mid + 1, j + 1]
                    if numbers[mid] > find:
                        y = mid - 1
                    else:
                        x = mid + 1
                i = x


# Solution 3. Use the builtin function
from bisect import bisect_left


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            value = numbers[i] + numbers[j]
            if value == target:
                return [i + 1, j + 1]

            if value > target:
                find = target - numbers[i]
                pos = bisect_left(numbers, find, i + 1, j)
                if numbers[pos] == find:
                    return [i + 1, pos + 1]
                j = pos - 1
            else:
                find = target - numbers[j]
                pos = bisect_left(numbers, find, i, j - 1)
                if numbers[pos] == find:
                    return [pos + 1, j + 1]
                i = pos
