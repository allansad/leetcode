class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # 시간복잡도: k번 반복하므로 O(k)
        # 공간복잡도: O(1)
        for i in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier

        return nums 