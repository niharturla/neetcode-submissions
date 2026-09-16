class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        maxlength=0
        seen = set()
        while r < len(s):
            while s[r] in seen:
                # move l until 
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxlength = max(maxlength, r-l+1)
            r += 1
        return maxlength
                
            
