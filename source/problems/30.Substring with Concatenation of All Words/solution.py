class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        matching = {}
        for word in words:
            if word in matching:
                matching[word] += 1
            else:
                matching[word] = 1

        word_length = len(words[0])
        word_count = len(words)
        s_length = len(s)
        result = []

        for i in range(0, s_length - word_length * word_count + 1, 1):
            start = i
            tmp_map = matching.copy()
            while tmp_map:
                target = s[start : start + word_length]
                if target in tmp_map:
                    if tmp_map[target] == 1:
                        tmp_map.pop(target)
                    else:
                        tmp_map[target] -= 1
                    start += word_length
                else:
                    break
            if not tmp_map:
                result.append(i)
        return result

