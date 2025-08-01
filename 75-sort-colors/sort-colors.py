class Solution:
    def sortColors(self, nums: List[int]) -> None:
        sortnum = self.mergesort(nums)
        for i in range(len(nums)):
            nums[i]=sortnum[i]
    def mergesort(self,arr: List[int])->List[int]:
        if len(arr)<=1:
            return arr
        mid = len(arr)//2
        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])

        return self.merge(left,right)
    def merge(self,left: List[int],right: List[int])->List[int]:
        result = []
        i = j = 0 
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result