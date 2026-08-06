class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token in operators:
                # do math
                a = int(stack.pop())
                b = int(stack.pop())
                res = -1
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = b - a
                elif token == '*':
                    res = a * b
                else:
                    res =  b / a
                stack.append(res)
            else:
                stack.append(token)
        return int(stack.pop())