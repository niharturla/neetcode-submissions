class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        chars = {'(':')', '[':']','{':'}'}

        for char in s:
            if char in chars:
                stack.append(char)
            else:
                # closing brace
                if stack != []:
                    last=stack.pop() # open brace
                    print(last)
                    if char != chars[last]:
                        return False
                else:
                    return False
        if stack == []:
            return True
        else:
            return False
