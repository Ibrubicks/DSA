class Solution:
    def isPalindrome(self, x: int) -> bool:
        l=[]
        if x<0:
            return False
        while x >0:
            l.append(x%10)
            x=x//10
        left = 0 
        right = len(l)-1
        while left<=right:
            if l[left]!=l[right]:
                return False
            left+=1
            right-=1
        return True