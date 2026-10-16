class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats, i, j = 0, 0, len(people) - 1
        while i < j:
            remaining_weight = limit - people[j]
            boats += 1
            j -= 1
            if i <= j and remaining_weight >= people[i]:
                i += 1
        if i == j:
            boats += 1
        return boats
