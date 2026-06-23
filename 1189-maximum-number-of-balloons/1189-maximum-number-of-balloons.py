class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_map = Counter(text)

        instance = len(text)

        for ch in "balloon":          
            if ch == "l" or ch == "o":
                instance = min(instance, text_map.get(ch, 0)//2)
            else:    
                instance = min(instance, text_map.get(ch, 0))

        return instance

