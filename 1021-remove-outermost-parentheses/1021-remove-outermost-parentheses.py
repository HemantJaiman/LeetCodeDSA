class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        output = ""
        depth = 0

        for ch in s:
            if ch == "(":
                if depth > 0:
                    output += ch
                depth +=1
            else:
                depth -=1
                if depth > 0:
                    output += ch
                
        return output