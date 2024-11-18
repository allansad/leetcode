class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # 시간복잡도: 배열의 각 요소(point)에 대해 O(nlogn)
        # 공간복잡도: O(n)
        temp_arr = []
        result_arr = []
        
        for i, point in enumerate(points):
            temp_arr.append((i, pow(point[0], 2)+pow(point[1], 2)))
        
        temp_arr.sort(key=lambda point: point[1])
        
        for i in range(k):
            result_arr.append(points[temp_arr[i][0]])

        return result_arr