class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
s = Solution()
print(s.search([4,5,6,7,0,1,2], target = 0))