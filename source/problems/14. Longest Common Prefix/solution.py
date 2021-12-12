class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs

        def common_prefix(a: str, b: str) -> int:
            length = min(len(a), len(b))
            for i in range(length):
                if a[i] != b[i]:
                    return i
            return length

        while len(result) > 1:
            tmp = []
            for i in range(0, len(result), 2):
                if i + 1 < len(result):
                    length = common_prefix(result[i], result[i + 1])
                    if length == 0:
                        return ""
                    tmp.append(result[i][:length])
                else:
                    tmp.append(result[i])
            result = tmp
        return result[0]