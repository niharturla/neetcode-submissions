class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        memo = {}
        def longest(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == m or j == n:
                return 0
            elif text1[i] == text2[j]:
                memo[(i,j)] = 1 + longest(i+1,j+1)
            else:
                memo[(i,j)] = max(longest(i,j+1), longest(i+1,j))
            return memo[(i,j)]
        return longest(0,0)