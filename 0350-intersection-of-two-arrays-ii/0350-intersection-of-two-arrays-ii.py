class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        result = []

        for i in nums2:
            if count[i] > 0:
                result.append(i)
                count[i] -= 1

        return result






