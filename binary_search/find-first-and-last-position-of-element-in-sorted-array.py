class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low = 0
        high = len(nums) - 1
        range_list = []

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]
            if guess == target:
                for i in range(low, high+1):
                    
                    if nums[i] == target:
                        range_list.append(i)
                break
            if guess > target:
                high = mid - 1
            elif guess < target:
                low = mid + 1
        sorted_list = sorted(range_list)
        if len(sorted_list) >= 2:
            return [sorted_list[0], sorted_list[-1]]
        elif len(sorted_list) == 1:
            return [sorted_list[0], sorted_list[0]]
        else:
            return [-1, -1]

s = Solution()
print(s.searchRange(nums = [1, 2,2], target = 2))