class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        past_totals = defaultdict(int)
        past_totals[0] = 1
        
        running_total = 0
        smaller_counts = 0
        winning_chains = 0
        
        for num in nums:
            old_total = running_total
            
            if num == target:
                running_total += 1
                # Since our total went UP, any past totals that were equal
                # to our old_total are now strictly smaller than our new total!
                smaller_counts += past_totals[old_total]
            else:
                running_total -= 1
                # Since our total went DOWN, any past totals that match our
                # brand new running_total are no longer smaller than it.
                smaller_counts -= past_totals[running_total]
                
            # Add all the smaller past totals we found to our final answer
            winning_chains += smaller_counts
            
            # Record our new running total into our history book
            past_totals[running_total] += 1
            
        return winning_chains
