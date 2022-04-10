class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        people.sort()
        while people:
            count+=1
            if people[0]+people[-1] <=limit:
                try:
                    people.pop(-1)
                    people.pop(0)
                except:
                    pass
            else:
                people.pop(-1)
        return(count)