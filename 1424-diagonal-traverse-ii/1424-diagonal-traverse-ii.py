class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # 시간복잡도: 
        # 공간복잡도: 

        temp = {}

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j not in temp:
                    temp[i + j] = []
                temp[i + j].append(nums[i][j])
        
        result_arr = []
        
        for key in temp.keys():
            result_arr.extend(reversed(temp[key]))
        
        return result_arr
        