import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return math.prod(map(int, list(str(n)))) - sum(map(int, list(str(n))))
