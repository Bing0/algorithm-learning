class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        result = list(s)

        while i < j:
            while i < j and (not (("a" <= s[i] <= "z") or ("A" <= s[i] <= "Z"))):
                i += 1

            while i < j and (not (("a" <= s[j] <= "z") or ("A" <= s[j] <= "Z"))):
                j -= 1
            result[i], result[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(result)
