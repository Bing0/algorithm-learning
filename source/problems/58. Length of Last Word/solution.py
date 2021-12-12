class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        i = 0
        j = -1
        while j < len(s):
            i = j + 1
            while i < len(s) and s[i] == " ":
                i += 1
            j = i + 1
            while j < len(s) and s[j] != " ":
                j += 1
            if i != len(s):
                ans = j - i
        return ans
