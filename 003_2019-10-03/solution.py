# Assumption 1: A palindrome is any string that has length >= 2
class Solution: 
    def longestPalindrome(self, s):
        palindromes = []
        for i in range(len(s)):
            for j in range(i+2, len(s)): # i + 2 due to Assumption 1
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    palindromes.append(temp)
        result = max(palindromes, key=len) if palindromes else None
        return result
        
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar