class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = { i:[] for i in range(numCourses)}
        output = []

        for src,dst in prerequisites:
            adj_list[src].append(dst)
        
        def dfs(src, path):
            if src in visit:
                return True
            if src in path:
                return False

            path.add(src)
            for dst in adj_list[src]:
                if not dfs(dst,path):
                    return False 
            path.remove(src)
            visit.add(src)
            output.append(src)
            return True

        visit = set()

        for crs in range(numCourses):
            if not dfs(crs, set()):
                return []
        
        return output