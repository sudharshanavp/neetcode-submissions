class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                int_1 = stack.pop()
                int_2 = stack.pop()
                res = int_2 + int_1
                stack.append(res)
            elif token == "-":
                int_1 = stack.pop()
                int_2 = stack.pop()
                res = int_2 - int_1
                stack.append(res)
            elif token == "*":
                int_1 = stack.pop()
                int_2 = stack.pop()
                res = int_2 * int_1
                stack.append(res)            
            elif token == "/":
                int_1 = stack.pop()
                int_2 = stack.pop()
                res = int(int_2 / int_1)
                stack.append(res)            
            else:
                stack.append(int(token))
        return stack.pop()