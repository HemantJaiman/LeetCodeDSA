class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        unique_costs = sorted(list(set(cost for _,_,cost in edges)))

        if not unique_costs:
            return -1

        adj_list = { i:[] for i in range(len(online))}
        for src,dst,cost in edges:
            if not online[src] or not online[dst]:
                continue
            adj_list[src].append([dst,cost])
        
        maximum_path_score = -1

        def find_path(threshold):
            min_heap = [[0,0]]  #[cost, destination]
            visit = set()

            while min_heap:
                curr_cost, src = heapq.heappop(min_heap)
                
                if src in visit:
                    continue
                visit.add(src)

                if src == len(online)-1:
                    return True
                
                for dst,next_cost in adj_list[src]:
                    if next_cost < threshold or next_cost+curr_cost > k or dst in visit:
                        continue
                    heapq.heappush(min_heap, [next_cost+curr_cost, dst])

            return False

        # using binary search
        l,r = 0, len(unique_costs)-1

        while l <= r:
            mid = (l+r)//2
            if find_path(unique_costs[mid]):
                maximum_path_score = unique_costs[mid]
                l = mid+1
            else:
                r = mid-1
        
        return maximum_path_score