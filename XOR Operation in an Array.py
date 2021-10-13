class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start+2*i for i in range(n)]
        out = nums[0]
        for i in range(1, n):
            out ^= nums[i]
        return out