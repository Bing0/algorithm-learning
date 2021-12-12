class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for c in s:
            if 'A' <= c <= "Z":
                ans += chr(ord(c) - ord('A') + ord('a'))
            else:
                ans += c
        return ans
