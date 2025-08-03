from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        j = 1
        for num in nums:
            if num <= 0:
                continue
            if num == j:
                j += 1
            elif num > j:
                return j
        return j
