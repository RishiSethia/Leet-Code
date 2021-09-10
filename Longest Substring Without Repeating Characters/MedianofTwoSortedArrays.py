class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = 0
        n2 = 0
        mergedList = []
        while True:
            if n1 == len(nums1):
                mergedList.extend(nums2[n2:])
                break
            if n2 == len(nums2):
                mergedList.extend(nums1[n1:])
                break             
            if nums1[n1] < nums2[n2]:
                mergedList.append(nums1[n1])
                n1 += 1
            else:
                mergedList.append(nums2[n2])
                n2 += 1

        if len(mergedList) % 2 == 0:
            return (mergedList[int(len(mergedList) / 2) - 1] + mergedList[int(len(mergedList) / 2)])/2
        else:
            return (mergedList[int(len(mergedList) / 2)])
			
clsObj = Solution()
res = clsObj.findMedianSortedArrays([1,3],[2])
