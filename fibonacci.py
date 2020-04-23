class Solution():
  def fibonacci(self, n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return Solution().fibonacci(n-1) + Solution().fibonacci(n-2)

n = 7
print(Solution().fibonacci(n))
# 34