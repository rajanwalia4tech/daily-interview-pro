class Solution:

    def lengthOfLongestSubstring(self, s):
        appearedChar = dict()
        start = 0
        end = 0
        seqPair = []
        seqLength = []

        for i, currentChar in enumerate(s):
            if currentChar not in appearedChar:
                appearedChar[currentChar] = i
                end = i
            else:
                if currentChar == s[i-1]:
                    start = i
                    end = i
                    appearedChar.clear()
                    appearedChar[currentChar] = i
                else:
                    start = appearedChar[currentChar] + 1
                    end = i
                    appearedChar = { k : v for k, v in appearedChar.iteritems() if v >= start } # removed unnecessary records
                    appearedChar[currentChar] = i
            seqPair.append((start, end))
            seqLength.append(end - start + 1)

        # print seqPair
        # print substrings for checking
        # for i in seqPair:   print s[i[0]:i[1]+1]
        return max(seqLength) if seqLength else 0 

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10
# print Solution().lengthOfLongestSubstring('asdfakfjsakldjsajksadjasjdlskdjala')