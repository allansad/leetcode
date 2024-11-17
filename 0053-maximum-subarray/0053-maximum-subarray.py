class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 시간복잡도: O(n)
        # 공간복잡도: 변수와 상관없이 상수값만 가지므로 O(1)

        if len(nums) == 0:
            return None 

        result = nums[0]
        comparison = nums[0]

        for i in range(1, len(nums)):
            comparison = max(nums[i], comparison+nums[i])

            result = max(result, comparison)

           
        return result