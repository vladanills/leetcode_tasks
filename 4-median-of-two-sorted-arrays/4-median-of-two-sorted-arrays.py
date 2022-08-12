class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = sorted(nums1 + nums2)
        len_array = len(merged_list)
        if len_array % 2 == 0:
            return (merged_list[len_array//2-1] + merged_list[len_array//2]) / 2
        else:
            return merged_list[len_array//2]
        return med