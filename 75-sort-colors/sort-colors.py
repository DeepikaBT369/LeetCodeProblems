class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                # swap 0 to the front
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                # already in correct middle region
                mid += 1

            else:  # nums[mid] == 2
                # swap 2 to the end
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1