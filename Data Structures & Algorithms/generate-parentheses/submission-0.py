class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        opens=0
        close=0

        def backtrack(opens,close,sol):
            if opens == n and close == n:
                res.append(sol)
                return
            # add '(' if open
            if opens < n:
                backtrack(opens+1, close, sol + "(")
            if close < opens:
                backtrack(opens, close+1, sol+")")
            
            

        backtrack(0,0,"")
        return res

