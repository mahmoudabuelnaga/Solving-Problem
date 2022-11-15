class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        full_list = [i for sub_list in matrix for i in sub_list]
        print(full_list)
        low = 0
        high = len(full_list) - 1
        print(high)
        
        while low <= high:
            mid = (low + high) // 2
            print(mid)

            guess = full_list[mid]

            if guess == target:
                return True
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1

        if len(full_list) == 1:
            if full_list[0] == target:
                return True
        return False

s = Solution()
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))