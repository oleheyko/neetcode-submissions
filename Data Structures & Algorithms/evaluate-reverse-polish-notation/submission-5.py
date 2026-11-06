class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                if token == "+":
                    result = stack.pop() + stack.pop()   
                elif token == "-":
                    result = - stack.pop() + stack.pop()
                elif token == "*":
                    result = stack.pop() * stack.pop()
                elif token == "/":
                    result = int((1 / stack.pop()) * stack.pop())
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]