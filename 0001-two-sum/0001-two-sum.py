class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            diff = t - nums[i]
            if diff in d:
                return d[diff] , i
                break
            d[nums[i]] = i