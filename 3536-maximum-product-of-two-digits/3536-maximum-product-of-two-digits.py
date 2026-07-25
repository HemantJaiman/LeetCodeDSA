class Solution:
    def maxProduct(self, n: int) -> int:
        if not n:
            return n
        
        product = 0

        first = 0
        second = 0

        for val in str(n):
            if int(val) > first:
                second, first = first, int(val)
            elif int(val) > second:
                second = int(val)

            product = max(first*second, product)
        
        return product
