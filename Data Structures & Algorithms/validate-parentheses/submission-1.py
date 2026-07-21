class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == "{":
                stack.append(char)
            elif char == "[":
                stack.append(char)
            elif char == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return stack == []
        