class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 시간복잡도: s의 길이에 대해 O(n^2)
        # 공간복잡도: numRows에 대해 O(n)

        if len(s) == 1 or numRows == 1:
            return s

        idx = 0
        flag = True
        temp = [""] * numRows

        for char in s:
            temp[idx] += char
            if idx == numRows - 1:
                flag = False
            if idx == 0:
                flag = True
            if flag == True:
                idx += 1
            if flag == False:
                idx -= 1

        return "".join(temp)

        
            