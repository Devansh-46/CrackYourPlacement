class Solution:
    def nextGreaterElement(self, nums1, nums2):
        results = [-1] * len(nums1)
        element_map = {num: i for i, num in enumerate(nums2)}

        for i, num in enumerate(nums1):
            current_index = element_map[num]
            current_element = num
            for j in range(current_index + 1, len(nums2)):
                if nums2[j] > current_element:
                    results[i] = nums2[j]
                    break

        return results
