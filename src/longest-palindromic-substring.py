'''
Author: Sundeep Babbur

Problem Link: https://leetcode.com/problems/longest-palindromic-substring/

Solution: Using `Manachers Algorithm` for O(n) time complexity.
  O(n^2) algorithm would be to expand across all the centers to find the
  longest palindromic substring.
  Manachers alogirthm modifies the above approach to achieve O(2n) i.e O(n)
  time complexity.
  Once we find the palindrome length for a center we will try to use the
  data we have gathered in this iteration to skip few centers.
  Since we have data of the left part of the current center and we use that
  data to fill the palindrome lengths for right part which fall in the
  palindrome part of the current center as both the left and right parts are
  like mirrors.
  The next center to be evaluated will be the index whose left mirror exactly
  expands till the left end of the current palindrome substring.
  We stop evaluating next centers when the current palindrome reaches till the
  end of input string.
'''

class Solution(object):
  # We augment our string to handle both even and odd length palindrome cases.
  # Ex. We convert aabccbade to $a$a$b$c$c$b$a$d$e$
  def augmentStr(self, s):
    augmented_str = '$'
    size = len(s)
    for i in range(size):
      augmented_str += (s[i] + '$')
    return augmented_str

  def longestPalindrome(self, s):
    mod_s = self.augmentStr(s)
    size = len(mod_s)
    pal_arr = [1] * size
    curr_center, max_i = 0, 0
    while True:
      # Finds the palindrome length at the current center
      offset = (pal_arr[curr_center] // 2)
      left = curr_center - (offset + 1)
      right = curr_center + (offset + 1)
      while (left >= 0) and (right < size) and (mod_s[left] == mod_s[right]):
        offset += 1
        left = curr_center - (offset + 1)
        right = curr_center + (offset + 1)

      pal_arr[curr_center] = 2 * offset + 1
      # Check if currently evaluated palindrome is the longest palindrome
      if pal_arr[curr_center] > pal_arr[max_i]:
        max_i = curr_center

      # At this point we know that there can't be any other palindromic
      # substring whose length will be greater than currently evaluated length
      # as we have reached the end of input string
      if curr_center + offset == size - 1:
        break

      # Finds next center to evaluate
      start = 1
      curr_pal_start_index = curr_center - offset
      curr_pal_end_index = curr_center + offset
      while (curr_center + start) <= curr_pal_end_index:
        mirror_index = curr_center - start
        curr_index = curr_center + start
        mirror_pal_start_index = mirror_index - pal_arr[mirror_index] // 2
        if curr_pal_start_index <= mirror_pal_start_index:
          pal_arr[curr_index] = pal_arr[mirror_index]
          if curr_pal_start_index == mirror_pal_start_index:
            curr_center = curr_index
            break
        else:
          pal_arr[curr_index] = (curr_pal_end_index - curr_index) * 2 + 1
        start += 1
      else:
        curr_center += 1

    # Get actual palindrome substring using `pal_arr`
    pal_len = pal_arr[max_i] // 2
    pal_start = (max_i - pal_len) // 2
    return s[pal_start:pal_start+pal_len]


def main():
  solution = Solution()
  s = 'babadada'
  print(solution.longestPalindrome(s))


if __name__ == "__main__":
  main()