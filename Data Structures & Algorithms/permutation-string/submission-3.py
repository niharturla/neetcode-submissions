class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        """
        my idea is to create an array of all frequencies of s1 at the start
        decrement frequencies from s1_string array for every match in the substring

        if at the end of the loop, there exists a moment when the s1_string is all 0s then return true since we found a permutation substring

        fixed window = len(s1)

        """
        l=0
        s1_freq = [0] * 26
        for c in range(len(s1)):
            idx = ord(s1[c]) - ord('a')
            s1_freq[idx] += 1
        
        s2_freq = [0] * 26
        for r in range(len(s2)):
            idx = ord(s2[r]) - ord('a')
            s2_freq[idx] += 1

            if r-l+1 > len(s1):
                idx = ord(s2[l]) - ord('a')
                s2_freq[idx] -= 1
                l += 1
            if s2_freq == s1_freq: return True
        return False
            