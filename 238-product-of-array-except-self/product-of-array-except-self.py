class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prod = math.prod(nums)
        zerocount = nums.count(0)
        prod1=1
        if zerocount > 1:
            return [0]*len(nums)
        for num in nums:
            if num!=0:
                prod1*=num
        for num in nums:
            if zerocount==0:
                result.append(prod//num)
            elif num==0:
                result.append(prod1)
            else:
                result.append(0)


        return result
