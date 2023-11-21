# Iterating by every item in nums: List is giving current_item,
#   current_item + x (searching number) = target
#   x (searching number) = target - current_item
#   if x in nums -> return idx of current_item anf idx of x

# RUNTIME: 382ms (regarding leetcode)
class Solution_0:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 2 and nums[0] + nums[1]:
            return [0, 1]

        for idx, current_item in enumerate(nums):
            x = target - current_item
            try:
                if nums.index(x, idx + 1, len(nums)):
                    return [idx, nums.index(x, idx + 1, len(nums))]
            except:
                print('none')

# RUNTIME: 61ms (regarding leetcode)
class Solution_1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #  E.g. [1, 2, 3]
        hashMap = {}
        for idx, current_item in enumerate(nums):
            x = target - current_item
            if x in hashMap:
                return [hashMap[x], idx]

            # Here assigning the value
            hashMap[nums[idx]] = idx