class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        output = 0
        
        last_a, last_b, last_c = -1, -1, -1

        for i, ch in enumerate(s):
            if ch == "a":
                last_a = i
            elif ch == "b":
                last_b = i
            else:
                last_c = i

            if last_a != -1 and last_b != -1 and last_c != -1:
                output += min(last_a, last_b, last_c) + 1
        
        return output