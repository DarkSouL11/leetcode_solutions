'''
Author: Sundeep Babbur

Problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Solution: Key to solving this problem is to rightly understand what median
  of an array is. Median of an array can be defined as an element/elements which
  divide the array into 2 equal halves so that all the elements on the left half
  are smaller than all the elements on the right of it.
  If array size is even then median is the element that divides the array.
  if array size is odd then two elements divide the array then median is the
  average of those two values.
'''

class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    max_val = 999999999999
    # Adding 2 numbers to an array i.e, one at the start and the other at the
    # end which wont change the sorted state of the array will also not change
    # the median of the array.
    # Using the above logic we add two extra numbers one at start and one at
    # end to the array so that we don't have to handle the edge cases manually
    nums1 = [-max_val] + nums1 + [max_val]
    nums2 = [-max_val] + nums2 + [max_val]

    len1 = len(nums1)
    len2 = len(nums2)

    if len1 > len2:
      return self.findMedianSortedArrays(nums2, nums1)

    low, high = 0, len1 - 1

    while low <= high:
      partition1 = (low + high) // 2
      partition2 = ((len1 + len2 + 1) // 2) - partition1 - 2

      # max value in the left partition that occurs from first array
      max_left_1 = nums1[partition1]
      # max value in the left partition that occurs from second array
      max_left_2 = nums2[partition2]
      # min value in the right partition that occurs from first array
      min_right_1 = nums1[partition1 + 1]
      # min value in the right partition that occurs from second array
      min_right_2 = nums2[partition2 + 1]

      if (max_left_1 <= min_right_2) and (max_left_2 <= min_right_1):
        if (len1 + len2) % 2 == 0:
          return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2
        else:
          return max(max_left_1, max_left_2)
      elif max_left_1 > min_right_2:
        high = partition1 - 1
      else:
        low = partition1 + 1


def main():
  solution = Solution()
  arr1 = [1, 2]
  arr2 = [3, 4]
  print(solution.findMedianSortedArrays(arr1, arr2))

if __name__ == "__main__":
  main()