'''
Author: Sundeep Babbur
'''

class Solution(object):
  def get_count(self, num_str):
    num_str_len = len(num_str)
    counts_arr = [0] * num_str_len
    for i in range(num_str_len):
      if i == 0:
        counts_arr[i] = 1
      else:
        curr_char = num_str[i]
        prev_char = num_str[i - 1]
        counts_arr[i] = counts_arr[i - 1]
        alt_char = int(prev_char + curr_char)
        if (alt_char > 9) and (alt_char < 26):
          if i == 1:
            counts_arr[i] += 1
          else:
            counts_arr[i] += counts_arr[i - 2]
    return counts_arr[num_str_len - 1]


def main():
  solution = Solution()
  s = '12023'
  print(solution.get_count(s))


if __name__ == "__main__":
  main()