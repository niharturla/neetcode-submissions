class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = 0

        """
        for each i we move out and check if these substrings are palindromes

        """
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                substrings += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                substrings += 1
                l -= 1
                r += 1
        return substrings

