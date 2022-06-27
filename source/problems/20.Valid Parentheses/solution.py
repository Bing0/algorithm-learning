class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            "(": ")",
            "{": "}",
            "[": "]"}

        for c in s:
            if c in valid:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if valid[stack[-1]] != c:
                    return False
                stack.pop(-1)
        if len(stack) != 0:
            return False
        return True


# Another similar solution
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
