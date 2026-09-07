class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        output = -1

        for l in range(len(s)):
            for r in range(l+1, len(s)):
                if s[l] == s[r]:
                    output = max(output, r-l-1)
        
        return output