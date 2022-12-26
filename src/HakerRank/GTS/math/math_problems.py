import math
from itertools import permutations, combinations


# --------------------------
# Region: Rationle
# --------------------------

def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def simplifyRationale(numerator, denominator):
    if denominator < 0 and numerator > 0:
        denominator = -denominator
        common_divisor = gcd(numerator, denominator)
        return [-numerator // common_divisor, denominator // common_divisor]
    elif numerator > 0 and denominator > 0:
        common_divisor = gcd(numerator, denominator)
        return [numerator // common_divisor, denominator // common_divisor]
    elif numerator < 0 and denominator > 0:
        numerator = -numerator
        common_divisor = gcd(numerator, denominator)
        return [-numerator // common_divisor, denominator // common_divisor]
    elif numerator == 0:
        return [numerator, 1]
    elif denominator < 0 and denominator < 0:
        denominator = -denominator
        numerator = -numerator
        common_divisor = gcd(numerator, denominator)
        return [numerator // common_divisor, denominator // common_divisor]


# --------------------------
# End Region: Rationle
# --------------------------

# --------------------------
# Region: Factorial
# --------------------------


def factorial(n):
    if n == 1:
        return 1
    else:

        return n * factorial(n - 1)


def leastFactorial(n):
    k = 1

    while factorial(k) <= n:
        fa = factorial(k)
        if fa >= n:
            return factorial(k)
        else:
            k += 1
    return factorial(k)


# --------------------------
# End Region: Factorial
# --------------------------

# --------------------------
# Region: Prime numbers
# --------------------------


def checkIfPrime(N):
    if N == 2:
        return 1
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return 0
    else:
        return 1


def primeCount(n):
    number_of_prime_factors = 0
    product_of_prime_factors = 1
    if n == 1:
        return 0
    if n == 2:
        return 1

    for i in range(2, n):
        if checkIfPrime(i) == 1:

            product_of_prime_factors *= i
            if product_of_prime_factors > n:
                break
            number_of_prime_factors += 1

    return number_of_prime_factors


# --------------------------
# End Region: Prime numbers
# --------------------------


# --------------------------
# Region: XOR
# not accepted by hakerrank.
# --------------------------
def strings_xor(s, t):
    res = []
    s_res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res.append('0')
        else:
            res.append('1')
    s_res = s_res.join(res)
    return s_res


def strings_xor_accepted(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1';

    return res


# --------------------------
# End Region: XOR
# --------------------------


def nearlySimilarRectangles(sides):
    count = 0
    for i in range(len(sides)):
        for j in range(i + 1, len(sides)):
            if sides[i][0] / sides[j][0] == sides[i][1] / sides[j][1]:
                count += 1
    return count


def findSubstring(s, k):
    d = {}
    res = [s[x:y] for x, y in combinations(range(len(s) + 1), r=2) if len(s[x:y]) == k]
    for sub in res:
        d.update({sub: sum([sub.count(x) for x in 'aeiou'])})
    if sum(d.values()) == 0:
        return 'Not Found!'
    else:
        re = max(d, key=d.get)

    return re


def tn(n):
    return n ** 2 - (n - 1) ** 2


def summingSeries(n):
    res = list(map(tn, range(1, n + 1)))
    return sum(res) % 10 ** 9 + 7

def calPascal(self, i, j):
        if j == 0 or j == i:
            return 1
        else:
            return self.calPascal(i - 1, j - 1) + self.calPascal(i - 1, j)

def generate(self, numRows: int):
        n_row = []
        for i in range(numRows):
            inner = []
            for j in range(i + 1):
                inner.append(self.calPascal(i, j))
            n_row.append(inner)
        return n_row




if __name__ == '__main__':
    findSubstring(s='qwdftr', k=2)
    nearlySimilarRectangles(sides=[[5, 10], [10, 10], [3, 6], [9, 9]])
    print('-*-' * 30)
    print('Simplify Rationale')
    print(simplifyRationale(-18, -24))
    print('-*-' * 30)
    print('Prime Count')
    print(primeCount(500))
    print('-*-' * 30)
    print('Least factorial')
    print(leastFactorial(17))
    print('-*-' * 30)
    print('XOR')
    print(strings_xor(s='10101', t='00101'))
    print(summingSeries(n=229137999))
    print('The END')
