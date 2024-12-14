class Solution:
    def findScore(self, nums: List[int]) -> int:
       # 시간복잡도: nums의 길이에 대해 O(n log n)
        # 공간복잡도: nums의 길이에 대해 O(n)
        score = 0
        temp = nums[:]
        n = len(temp)
        processed = [False] * n
        heap = []
        
        for i, num in enumerate(temp):
            heappush(heap, (num, i))
        
        while heap:
            min_val, index = heappop(heap)
            if processed[index]:
                continue
            score += min_val
            processed[index] = True
            if index - 1 >= 0:
                processed[index - 1] = True
            if index + 1 < n:
                processed[index + 1] = True
        
        return score