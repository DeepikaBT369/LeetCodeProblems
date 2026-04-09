from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
        # result=set()
        # nums2_set=set(nums2)

        # for num in nums1:
        #     if num in nums2_set:
        #         result.add(num)

        # return list(result)
