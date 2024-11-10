class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # 시간복잡도: 
        # 공간복잡도:

        start = image[sr][sc]

        def recursion(i, j):
            if i >= len(image) or j >= len(image[i]) or i < 0 or j < 0:
                return

            current = image[i][j]
            
            if current != start or current == color:
                return

            image[i][j] = color

            recursion(i, j-1)
            recursion(i, j+1)
            recursion(i-1, j)
            recursion(i+1, j)


        recursion(sr, sc)

        return image

        