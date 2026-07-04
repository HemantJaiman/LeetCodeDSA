class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        adj_list = {i:[] for i in range(1, n+1)}

        for src,dst,distance in roads:
            adj_list[src].append([dst,distance])
            adj_list[dst].append([src,distance])

        global_score = [float("inf")]
        visit  = set()

        def dfs(src):
            
        
            visit.add(src)
            for dst,distance in adj_list[src]:
                global_score[0] = min(global_score[0], distance)
                if dst not in visit:
                    dfs(dst)
            return

        dfs(1)
        return global_score[0]