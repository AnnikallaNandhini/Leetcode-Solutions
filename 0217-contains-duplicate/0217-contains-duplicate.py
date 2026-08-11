class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for i in d.values():
            if i > 1:
                return True
                break
        else:
            return False
        