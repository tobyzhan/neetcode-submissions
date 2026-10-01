class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            
            else: 
                if not stack:
                    return False
                
                if char in ")}]" and len(stack) > 0:
                    if char == ")" and stack[-1] == "(":
                        stack.pop(-1)
                    elif char == "}" and stack[-1] == "{":
                        stack.pop(-1)
                    elif char == "]" and stack[-1] == "[":
                        stack.pop(-1)
                    else:
                        return False
        
        if len(stack) > 0:
            return False

        return True
                