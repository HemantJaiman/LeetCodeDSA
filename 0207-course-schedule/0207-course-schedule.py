class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}

        for src,dst in prerequisites:
            adj_list[src].append(dst)
        
        def dfs(crse,path):
            if crse in path:
                return False
            path.add(crse)

            for dst in adj_list[crse]:
                if not dfs(dst,path):
                    return False
            path.remove(crse)
            adj_list[crse] = []
            return True
            
        

        for crse in range(numCourses):
            if not dfs(crse, set()):
                return False
        
        return True