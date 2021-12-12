class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in pair:
                if len(stack) == 0 or pair[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True
