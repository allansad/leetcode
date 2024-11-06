class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return_value = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[return_value] = nums[i]
                return_value += 1
        return return_value