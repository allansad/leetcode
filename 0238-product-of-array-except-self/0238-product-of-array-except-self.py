class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 시간복잡도: list의 길이에 대해 O(n)
        # 공간복잡도: list의 길이에 대해 O(n)

        result = []

        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(math.prod([e for j, e in enumerate(nums) if j != i]))
            else:
                result.append(int(math.prod(nums) * pow(nums[i], -1)))


        return result

        