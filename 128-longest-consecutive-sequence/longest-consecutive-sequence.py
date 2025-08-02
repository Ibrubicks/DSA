class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        count = 1
        maxcount = 1
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)):
            if abs(nums[i-1]-nums[i])==1:
                count+=1
                maxcount = max(count,maxcount)
            else:
                count = 1
        return maxcount