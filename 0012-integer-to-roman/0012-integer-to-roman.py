class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 시간복잡도: num값에 대해 O(n)
        # 공간복잡도: 입력 크기와 상관없이 정해진 공간(temp_arr)만 사용하기 때문에 O(1)
        
        temp_arr = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        result = ""

        for value, symbol in temp_arr:
            while num >= value:
                result += symbol
                num -= value
        
        return result