class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        l = 0
        freq = [0] * 26
        max_f = 0
        for r in range(n):
            
            freq[ord(s[r]) - ord('A')] += 1
            max_f = max(max_f, freq[ord(s[r]) - ord('A')])
            while (r - l + 1) - max_f > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r-l+1)
        return res


