class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new = []
        maxm = max(candies)
        for i in candies:
            new.append(i+extraCandies >= maxm)
        return new