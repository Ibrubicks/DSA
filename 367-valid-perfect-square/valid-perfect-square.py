import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = math.sqrt(num)
        if n==int(n):
            return True
        else:
            return False