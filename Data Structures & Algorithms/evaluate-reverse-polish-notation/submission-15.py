class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        ops ={
            "+":lambda a,b: b + a,
            "-":lambda a,b: b - a,
            "*":lambda a,b: b * a,
            "/":lambda a,b: int(b / a),
        }

        for token in tokens:
            print(stack)
            if token.lstrip("-").isnumeric():
                stack.append(int(token))
            
            if token in ["+","-","*","/"]:
                tempA = stack.pop()
                tempB = stack.pop()
                
                stack.append(ops[token](tempA,tempB)) 

        return(stack[-1])
        