class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_nodes = sorted((val,idx) for idx,val in enumerate(nums))
        # We need a quick way to look up where an original index is in our sorted list
        orig_to_sorted = [0] * n
        for sorted_idx, (val, orig_idx) in enumerate(sorted_nodes):
            orig_to_sorted[orig_idx] = sorted_idx
        
        R = [0] * n
        right = 0
        for left in range(n):
            # Move the 'right' pointer as far right as possible within maxDiff
            while right < n and sorted_nodes[right][0] - sorted_nodes[left][0] <= maxDiff:
                right += 1
            # 'right' stopped at the first invalid pad, so right - 1 is our furthest valid 1-jump
            R[left] = right - 1
        
        LEVELS = 18  
        # Create a 2D grid filled with zeros: jump_table[level][pad]
        jump_table = [[0] * n for _ in range(LEVELS)]
        
        # Level 0 means 2^0 = 1 jump. We already calculated this in array R!
        for pad in range(n):
            jump_table[0][pad] = R[pad]
            
        # Fill in the rest of the levels using the Doubling Trick
        for level in range(1, LEVELS):
            for pad in range(n):
                # To make a giant jump, first make a half-sized jump...
                midway_pad = jump_table[level - 1][pad]
                # ...then make another half-sized jump from that midway point!
                jump_table[level][pad] = jump_table[level - 1][midway_pad]
        
        output = []
        for u, v in queries:
            if u == v:
                output.append(0)
                continue
                
            # Convert original names to our sorted lineup positions
            start = orig_to_sorted[u]
            target = orig_to_sorted[v]
            
            # Ensure we are always moving from left to right
            if start > target:
                start, target = target, start
                
            total_jumps = 0
            curr = start
            
            # Try pressing shortcut buttons from largest (Level 17) down to smallest (Level 0)
            for level in range(LEVELS - 1, -1, -1):
                # If pressing this button keeps us safely strictly to the left of our target...
                if jump_table[level][curr] < target:
                    # ...press it! Teleport forward.
                    curr = jump_table[level][curr]
                    total_jumps += (1 << level)  # This is a fast way to write 2^level
            
            # We are now sitting exactly one final tiny jump away from our target.
            # Let's see if 1 last optimal jump (Level 0) can reach or cross the target.
            if jump_table[0][curr] >= target:
                output.append(total_jumps + 1)
            else:
                # Target is blocked by a gap larger than maxDiff
                output.append(-1)
                
        return output