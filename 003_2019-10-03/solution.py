# Assumption 1: A palindrome is any string that has length >= 2
class Solution: 
    def longestPalindrome(self, s):
        palindromes = []
        for i, currentChar in enumerate(s):
            for j in range(i+2, len(s)+1): # i + 2 due to Assumption 1
                temp = s[i:j]
                if temp == temp[::-1]:
                    palindromes.append(temp)
        result = max(palindromes, key=len) if palindromes else None
        return result
        
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar