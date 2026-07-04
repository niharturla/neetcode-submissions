class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left=0
        chars=set()
        maxlength=0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            maxlength=max(right-left+1,maxlength)
        return maxlength