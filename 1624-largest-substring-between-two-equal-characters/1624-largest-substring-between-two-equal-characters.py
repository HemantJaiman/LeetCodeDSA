class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        s_map = {}
        output = -1
        for i in range(len(s)):
            if s[i] in s_map:
                output = max(output, i - s_map[s[i]] - 1)
            else:
                s_map[s[i]] = i        
        return output 