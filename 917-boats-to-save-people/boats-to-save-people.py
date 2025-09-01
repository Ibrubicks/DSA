class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people)-1
        people.sort()
        boatcount = 0
        while l<=r:
            if people[l]+people[r] <= limit:
                boatcount +=1
                l+=1
                r-=1
            else:
                boatcount +=1
                r-=1
        return boatcount
