class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total, new = 0, []
        for num in nums:
            total += num
            new.append(total)
        return new