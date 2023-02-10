class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
            
        while i < m or j < n:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    arr.append(nums1[i])
                    i += 1
                else:
                    arr.append(nums2[j])
                    j += 1
            elif i < m:
                arr.append(nums1[i])
                i += 1
            elif j < n:
                arr.append(nums2[j])
                j += 1
        
        k = len(arr)
        if k % 2 == 0:
            return (arr[k // 2 - 1] + arr[(k // 2)]) / 2
        return float(arr[k // 2])
        
