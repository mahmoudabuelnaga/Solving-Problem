class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        small_friend_number = 0
        friend_number = 0

        if target > nums[high]:
            ind = len(nums)
            return ind
        elif target < nums[low]:
            return 0

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                print('=')
                return mid
            
            elif guess+1 == target:
                print('+')
                friend_number = mid + 1

            elif guess-1 == target:
                print('-')
                friend_number = mid

            
            if guess > target:
                high = mid - 1
            else:
                low = mid +1
        return friend_number

s = Solution()
# [1,2,3,4,5,10] [1,3,5,6] [2,3,4,7,8,9]
print(s.searchInsert(nums = [1,2,3,4,5,10], target = 2))
