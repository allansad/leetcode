class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 시간복잡도: sorted함수를 두번 호출하기 때문에 O(nlogn)
        # 공간복잡도: 문자열의 길이만큼 리스트의 크기가 증가하므로 O(n)

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t