class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        if n== 0:
            return 0

        output = "".join(str(n).split("0"))

        n_sum = 0

        for val in output:
            n_sum += int(val)
        
        return  int(output) * n_sum