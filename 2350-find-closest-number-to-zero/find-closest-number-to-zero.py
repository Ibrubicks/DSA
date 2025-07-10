class Solution:
    def findClosestNumber(self, nums):
        #ibrahim
        low = nums[0]
        for i in nums[1:]:
            if abs(i) < abs(low):
                low = i
            elif abs(i) == abs(low) and i > low:
                low = i
        return low
