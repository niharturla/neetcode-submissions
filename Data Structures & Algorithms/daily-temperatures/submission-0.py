class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # start backwards from the array

        # [28,40,35,36,30,38,30]
        # have a window length of at least 1
        
        """

        38 36
        We have temp
        Add temp to stack 
        get next_temp
        if next_temp greater than stack.top(), pop the stack
        append (next_temp_index - stack_index)

        """

        res = [0] * len(temperatures)
        stack=[]

        for i,t in enumerate(temperatures):
            
            while stack and stack[-1][0] < t:
                temp, index = stack.pop()
                res[index] = abs(i-index)
            stack.append((t,i))
        return res


