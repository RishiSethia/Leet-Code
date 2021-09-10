class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        subStr = ''
        tmp = ''
        for i in s:
            if i in tmp:
                if len(tmp) >= len(subStr):
                    subStr = tmp
                    tmp = tmp.split(i)[-1] + i
                else:
                    tmp = tmp.split(i)[-1] + i
            else:
                tmp += i
        if len(tmp) > len(subStr):
            subStr = tmp
        return len(subStr)

lString = Solution()
res = lString.lengthOfLongestSubstring("jbpnbwwd")
print(res)