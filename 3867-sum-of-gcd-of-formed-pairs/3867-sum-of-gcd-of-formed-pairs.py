class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            prefix_gcd.append(gcd(x, mx))

        prefix_gcd.sort()

        ans = 0
        l, r = 0, len(prefix_gcd) - 1

        while l < r:
            ans += gcd(prefix_gcd[l], prefix_gcd[r])
            l += 1
            r -= 1

        return ans