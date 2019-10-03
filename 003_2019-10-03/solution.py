# Assumption 1: A palindrome is any string that has length >= 2

class Solution: 
    def longestPalindrome(self, s):
        palindromes = []
        for i, currentChar in enumerate(s):
            for j in range(i+2, len(s)+1): # i + 2 due to Assumption 1
                temp = s[i:j]
                if isPalindrome(temp):
                    palindromes.append(temp)
        result = max(palindromes, key=len) if palindromes else None
        return result


def isPalindrome(s):
    midPoint = int (len(s)/2)
    return s[0:midPoint] == s[:midPoint-1:-1] if len(s) % 2 == 0 else s[0:midPoint] == s[:midPoint:-1]
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar