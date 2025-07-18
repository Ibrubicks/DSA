from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        freq = 0
        res = None
        for num in count:
            if count[num] > freq:
                freq = count[num]
                res = num
        return res