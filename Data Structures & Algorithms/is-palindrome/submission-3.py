class Solution:
    def isPalindrome(self, s: str) -> bool:

        '''
        This solution uses O(n) time complexity but O(n) space. Because
        we are allocating a new string of len n with the removal of
        all non-alphanumeric character.
        '''
        #s = "".join(char for char in s if char.isalnum()).lower()
        
        left=0
        right=len(s)-1
        print(s)
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            right -=1
            left += 1
        return True

        '''
        This solution is O(n) time and O(1) space
        ''' 
        