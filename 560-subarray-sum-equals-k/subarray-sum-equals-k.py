from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1 

        for num in nums:
            current_sum += num
            count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] += 1

        return count
