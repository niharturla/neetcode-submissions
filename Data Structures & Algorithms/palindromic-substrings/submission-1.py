class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # dp[i][j] is if s[i:j+1] is a substring

        # s[i:j+1] is a substring iff 
        # a) s[i] = s[j] and dp[i+1][j-1] == True

        # since we each dp state depends on its outer boundaries, we start i to n-1 and j to 0
        res = []
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
                    res.append(s[i:j+1])
                    dp[i][j] = True
        return len(res)
       

