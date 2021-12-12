class Solution:
    def reverseWords(self, s: str) -> str:
        r = len(s) - 1
        l = len(s)

        result = []

        while l > 0:
            r = l - 1
            while r >= 0 and s[r] == " ":
                r -= 1
            if r < 0:
                break
            l = r - 1

            while l >= 0 and s[l] != " ":
                l -= 1

            result.append(s[l + 1: r + 1])
        return " ".join(result)