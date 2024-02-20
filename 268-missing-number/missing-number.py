class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        og_list = [i for i in range(0, len(nums)+1)]
        left = set(og_list) - set(nums)
        return list(left)[0]
