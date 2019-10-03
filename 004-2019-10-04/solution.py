class Solution:
  def isValid(self, s):
        parentheses = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                parentheses.append(i)
            else:
                x = parentheses.pop()
                if x == '(' and i == ')' :
                    pass
                elif x == '{' and i == '}' :
                    pass
                elif x == '[' and i == ']' :
                    pass
                else:
                    return False
        return False if parentheses else True

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))