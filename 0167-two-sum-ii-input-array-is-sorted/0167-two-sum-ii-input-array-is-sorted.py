class Solution:
    def twoSum(self, nums: List[int], tar: int) -> List[int]:
        l = 0
        h = len(nums) - 1
        while l < h:
            if nums[l] + nums[h] == tar:
                return l+1 , h +1
            elif nums[l] + nums[h] > tar:
                h -= 1
            elif nums[l] + nums[h] < tar:
                l += 1
            else:
                l += 1
                h -= 1

