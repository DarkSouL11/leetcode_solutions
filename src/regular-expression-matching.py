'''
Author: Sundeep Babbur

Problem Link: https://leetcode.com/problems/regular-expression-matching.py/
'''

class Solution(object):
  def isMatch(self, s: str, p: str) -> bool:
    if s == '':
      return True
    if p == '':
      return False

    p_len = len(p)
    s_len = len(s)

    def matchHelper(s_i, p_i):
      p_end = p_i == p_len
      s_end = s_i == s_len
      if p_end or s_end:
        return (p_end and s_end)

      print(s_i, s[s_i], s_end, p_i, p[p_i], p_end)

      if (p_i + 1 == p_len) or (p[p_i + 1] != '*'):
        if (p[p_i] == '.') or (s[s_i] == p[p_i]):
          return matchHelper(s_i + 1, p_i + 1)
      else:
        k = 0
        while True:
          if (s_i + k == s_len):
            break

          if matchHelper(s_i, p_i + 2):
            return True

          if (p[p_i] == '.') or (p[p_i] == s[s_i + k]):
            if (matchHelper(s_i + k, p_i)):
              return True
          k += 1

      return False

    return matchHelper(0, 0)


def main():
  solution = Solution()
  string = 'mississippi'
  pattern = 'mis*.*p*i'
  print(solution.isMatch(string, pattern))


if __name__ == "__main__":
  main()