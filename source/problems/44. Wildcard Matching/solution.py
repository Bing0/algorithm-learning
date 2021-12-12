class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = " " + s
        p = " " + p

        n = len(s)
        m = len(p)

        dp = [[False for _ in range(m)] for _ in range(n)]

        dp[0][0] = True

        for j in range(1, m):
            if p[j] == "*":
                dp[0][j] = True
            else:
                break

        for i in range(1, n):
            for j in range(1, m):
                if s[i] == p[j] or p[j] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j] == "*":
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[n - 1][m - 1]