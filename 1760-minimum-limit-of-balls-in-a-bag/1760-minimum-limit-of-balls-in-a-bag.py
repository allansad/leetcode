class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # 시간복잡도: nums요소의 최대값에 대해 O(nlogn)
        # 공간복잡도: O(1)
        
        def can_divide(limit):
            operations = 0
            for num in nums:
                operations += (num - 1) // limit
                if operations > maxOperations:
                    return False
            return True
        
        left = 1
        right = max(nums)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if can_divide(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
