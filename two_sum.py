class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        # for n in nums:
        #     print(n)
        # for s in nums:
        #     print(s)
        #     if n+s == target:
        #         i1 = nums.index(n)
        #         i2 = nums.index(s)
        #         # l.append(i1, i2)
        #         # print(l)
        #         break

s = Solution()
s.twoSum([2,7,11,15],9)




#1- defined a varibels (nums:list, target:int, outPut of list :int)
#2- for loop on the list
#3- if condition for to calculate numbers of target
#4- return the index of numbers (list:int)