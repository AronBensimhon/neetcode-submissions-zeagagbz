class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for char in s.strip().lower():
            if char.isalnum() == True:
                temp += char
        l = 0
        r = len(temp) - 1
        print(temp)
        while l < r:
            if temp[l] != temp[r]:
                return False
            l += 1
            r -= 1
        return True