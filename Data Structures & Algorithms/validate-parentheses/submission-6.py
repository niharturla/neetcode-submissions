class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        chars = {'(':')', '[':']','{':'}'}

        for char in s:
            if char in chars:
                stack.append(char)
            else:
                # closing brace
                if not stack:
                    return False

                last=stack.pop()

                if char != chars[last]:
                    return False
        return len(stack) == 0
