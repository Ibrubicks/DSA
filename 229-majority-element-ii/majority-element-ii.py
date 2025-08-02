from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = []
        th = len(nums)//3
        for num,freq in count.items():
            if freq>th:
                result.append(num)
        return result
