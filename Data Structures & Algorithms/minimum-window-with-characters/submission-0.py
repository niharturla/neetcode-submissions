class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for c in t:
            countT[c] = countT.get(c,0) + 1
        window = {}

        """
        Once the window contains everything in t, move l to the right
        """

        l = 0

        have = 0
        need = len(countT)
        resLen = float("inf")
        res = ""

        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                # current window is valid
                if r - l + 1 < resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                leftChar = s[l]
                window[leftChar] -= 1
                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1
                l += 1
        return res

        # when a character reaches its freq,increase have

        # once have == need, shrink 



            
        
            
        
                
            