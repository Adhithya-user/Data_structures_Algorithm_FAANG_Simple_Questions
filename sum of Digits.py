"""def sumofDigits(n):
  assert n>=0 and int(n)==n,'The number has to be a positive only!'
  if n==0:
    return 0
  else:
    return int(n%10)+sumofDigits(int(n//10))

print(sumofDigits(1234))"""


def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "The number has to be positive only!"
    if n == 0:
        return 0
    else:
        return n % 10 + sumOfDigits(n // 10)

print(sumOfDigits(11))
