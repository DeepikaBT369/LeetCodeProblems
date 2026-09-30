class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # left = 0
        # right = len(nums) - 1

        # while left<=right:
        #     mid = (left+right)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid+1
        #     else:
        #         right = mid-1
        # return -1

        # left = 0
        # right = len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return -1


        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
                # because we have to return the index and not the number
                #  also we use nums[mid] because we should know the value of the mid and not the index to compare with the target
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

