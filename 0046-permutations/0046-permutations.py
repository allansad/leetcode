class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 시간복잡도: 재귀를 n번 돌면서 순열 개수가 n!이므로 O(n*n!)
        # 공간복잡도: result에 모든 순열을 저장하기 때문에 O(n*n!)
        result = []
        
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return result
        