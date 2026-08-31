class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x+y < target or target < 0:
            return False
        
        queue = deque()
        visit = set()
        visit.add(0)
        queue.append(0)

        operations = [x,-x,y,-y]

        while queue:
            curr = queue.popleft()
            if curr==target:
                return True
            
            for op in operations:
                nxt = curr + op
                if 0 < nxt <= x+y and nxt not in visit:
                    visit.add(nxt)
                    queue.append(nxt)
        
        return False