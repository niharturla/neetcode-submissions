class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time: O(n^3)
        Space: O(n)

        maxLength = 0
        res = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                l, r = i,j
                while l < r and s[l] == s[r]:
                    l +=1
                    r -= 1
                if l >= r and maxLength < (j - i + 1):
                    res = s[i:j+1]
                    maxLength = j - i + 1
                    
        return res
        """

        """
        Use DP to remember states of palindrome
        """
        resIdx, resLen = 0,0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    if resLen <(j-i+1):
                        resLen=j-i+1
                        resIdx = i
        return s[resIdx:resIdx+resLen]
        