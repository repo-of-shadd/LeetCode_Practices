class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        items = set()
        
        for i in range(len(nums)):
            if nums[i] in items:
                return True
            else:
                items.add(nums[i])
                
        return False