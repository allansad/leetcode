class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # 시간복잡도: 
        # 공간복잡도: 

        result_arr = []

        for arr in intervals:
            if arr[1] < newInterval[0]:
                result_arr.append(arr)
            elif arr[0] > newInterval[1]:
                result_arr.append(newInterval)
                newInterval = arr
            else:
                newInterval[0] = min(newInterval[0], arr[0])
                newInterval[1] = max(newInterval[1], arr[1])

        result_arr.append(newInterval)

        return result_arr
            
                

        


        