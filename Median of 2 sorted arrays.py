"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if(len(nums1)%2==0):
            lst_required=nums1[(len(nums1)//2)-1:(len(nums1)//2)+1]
            print(lst_required)
            result = sum(lst_required)/len(lst_required)
            print(f"result = {result}")
            return result
        else : 
            result=nums1[(len(nums1)//2)]
            print(f"result = {result}")
            return result
