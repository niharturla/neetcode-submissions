class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        """
        my idea is to create an array of all frequencies of s1 at the start
        decrement frequencies from s1_string array for every match in the substring

        if at the end of the loop, there exists a moment when the s1_string is all 0s then return true since we found a permutation substring

        """

        s1_freq = [0] * 26
        for c in range(len(s1)):
            idx = ord(s1[c]) - ord('a')
            s1_freq[idx] += 1
        
        for r in range(len(s2) - len(s1) + 1):
            # take substring of len(s1)
        
            freq = [0] * 26
            limit = len(s1) + r
            while r < limit:
                idx = ord(s2[r]) - ord('a')
                freq[idx] += 1
                r += 1
            
            if freq == s1_freq:
                return True
            
        return False

            