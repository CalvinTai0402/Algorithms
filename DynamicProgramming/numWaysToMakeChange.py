# O(2^d) T O(2^d) S where d is the length of denoms
def numberOfWaysToMakeChange(n, denoms):
    length = len(denoms)
    return numberOfWaysToMakeChangeR(n, denoms, length)


def numberOfWaysToMakeChangeR(n, denoms, length):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if length <= 0 and n >= 1:
        return 0
    return numberOfWaysToMakeChangeR(
        n - denoms[length - 1], denoms, length
    ) + numberOfWaysToMakeChangeR(n, denoms, length - 1)
    # Either you use the coin, or you don't use the coin at index length


# O(N*d) T O(N) S, N=n, d=denoms's length
def numberOfWaysToMakeChange2(n, denoms):
    ways = [0 for i in range(n + 1)]  # O(N) ?
    ways[0] = 1
    for denom in denoms:  # O(d)
        for amount in range(1, n + 1):  # O(N)
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]
