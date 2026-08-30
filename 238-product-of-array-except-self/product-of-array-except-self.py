class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        answer = [1] * n

        prefix = 1 #good to initiate to 1 so that we can multiply it, anyway we end up multiplying them all so
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
# the solution is product of 2 sides that is -> product of digits on the left side and product of the digit on the right side
# you need to take a digit and check on left and multiply the products, and then check on right and multiply those products and then take multiplication or product of both left and right


