class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #시간복잡도: magazine의 길이에 대해 O(n)
        #공간복잡도: magazine의 길이에 대해 O(n)
        temp_object = {}

        for char in magazine:
            temp_object[char] = 1 + temp_object.get(char, 0)

        for char in ransomNote:
            if char not in temp_object or temp_object[char] <= 0:
                return False
            temp_object[char] -= 1

    
        return True

        