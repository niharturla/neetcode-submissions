class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        l = 0
        counts= {}
        max_f = 0
        for r in range(n):
            
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_f = max(max_f, counts[s[r]])
            while (r - l + 1) - max_f > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res


