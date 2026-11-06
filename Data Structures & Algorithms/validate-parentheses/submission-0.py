class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                diff = ord(c) - ord(stack[-1])
                if (c == ')' and diff == 1) or (c in ']}' and diff == 2):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0