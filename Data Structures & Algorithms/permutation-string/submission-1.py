class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        """
        my idea is to create an array of all frequencies of s1 at the start
        decrement frequencies from s1_string array for every match in the substring

        if at the end of the loop, there exists a moment when the s1_string is all 0s then return true since we found a permutation substring

        """
    
        sorted_s1 = "".join(sorted(s1))

        for r in range(len(s2) - len(s1) + 1):
            # take substring of len(s1)
            substring = s2[r:len(s1)+r]
            if "".join(sorted(substring)) == sorted_s1:
                return True
        return False

            