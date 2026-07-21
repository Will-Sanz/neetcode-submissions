class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # set up the mapping of the closing symbol to the open symbol
        mapping = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        for char in s:
            # if it's an open symbol
            if char not in mapping:
                stack.append(char)
            else:
                # if the stack is empty
                if not stack:
                    return False
                # if the open symbol isn't the last thing
                if mapping[char] != stack.pop():
                    return False
        # if the stack is empty at the end, return True
        return not stack
        