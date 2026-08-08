class Solution:

    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        return int(y / x)
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return y-x

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'-':self.sub, '+':self.add, '/': self.divide, '*':self.multiply}
        stack=[]
        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            else:
                o1=stack.pop()
                o2=stack.pop()

                result = operators[tok](o1,o2)
                stack.append(result)
        return stack[0]

                
            
        
