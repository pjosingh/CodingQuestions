class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            print(i, primes, sum(primes))
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
                print("post: \t", i, primes, sum(primes))
        return sum(primes)

sol = Solution()
assert sol.countPrimes(10) == 4
