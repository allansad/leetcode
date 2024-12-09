class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 시간복잡도: nums의 길이에 대해 O(n)
        # 공간복잡도: nums의 길이에 대해 O(n)
        
        temp_max = 0
        result = 0
        temp_hash = {0: -1}

        for i, num in enumerate(nums):
            if num == 0:
                temp_max -= 1
            else:
                temp_max += 1
            if temp_max in temp_hash:
                result = max(result, i - temp_hash[temp_max])
            else:
                temp_hash[temp_max] = i
        return result
                    