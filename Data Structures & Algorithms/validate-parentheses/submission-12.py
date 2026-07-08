class Solution:
    def isValid(self, s: str) -> bool:
        
        parentDict = { "]" : "[","}" : "{", ")" : "(" }
        stack = []
        for c in s:
            if c in parentDict:
                if stack and stack[-1] == parentDict[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)
        return True if not stack else False