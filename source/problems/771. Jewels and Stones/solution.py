class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count_l = [0] * 26
        count_C = [0] * 26

        for s in stones:
            if s <= 'Z':
                count_C[ord(s) - ord('A')] += 1
            else:
                count_l[ord(s) - ord('a')] += 1

        ans = 0

        for j in jewels:
            if j <= 'Z':
                ans += count_C[ord(j) - ord('A')]
            else:
                ans += count_l[ord(j) - ord('a')]

        return ans
