class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + end - start + 1 / 2
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid
        if nums[start] == target:
            return start
        else:
            return -1
        

        

            
            