class Solution:
    def getWhile(self, left, right, res, s):
        tmp = None
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(res):
                tmp = s[left:right+1]
            left -= 1
            right += 1
        return tmp
        
    def longestPalindrome(self, s: str) -> str:
        resLong = ''
        
        for i in range(len(s)):
            left, right = i, i
            res = self.getWhile(left, right, resLong, s)
            if res:
                resLong = res

            left, right = i, i+1
            res = self.getWhile(left, right, resLong, s)
            if res:
                resLong = res
        return resLong

res = Solution()
longRes = res.longestPalindrome('abbab')
print(longRes)