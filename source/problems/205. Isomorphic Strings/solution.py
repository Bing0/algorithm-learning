class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        fa = [-1 for _ in range(128)]
        used = [False for _ in range(128)]

        for i in range(len(s)):
            si = ord(s[i])
            ti = ord(t[i])

            if fa[si] != ti and (used[ti] == True or fa[si] != -1):
                return False
            fa[si] = ti
            used[ti] = True
        return True
