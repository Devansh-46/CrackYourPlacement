class Solution:
    def isValid(self, s: str) -> bool:
        b = list()
        for i in s:
            if i == "(":
                b.append('(')
            elif i == ")":
                if len(b) >= 1 and b[-1] == "(":
                    b.pop()
                else:
                    return False
            elif i == "[":
                b.append('[')
            elif i == "]":
                if len(b) >= 1 and b[-1] == "[":
                    b.pop()
                else:
                    return False
            elif i == "{":
                b.append('{')
            elif i == "}":
                if len(b) >= 1 and b[-1] == "{":
                    b.pop()
                else:
                    return False
        if len(b) == 0:
            return True
        return False
        
