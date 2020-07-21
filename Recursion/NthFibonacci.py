# O(2^N) T O(N) S, O(N) S because each call calls another call on the call stack
def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return getNthFib(n - 1) + getNthFib(n - 2)


# O(N) T O(N) S
def getNthFib2(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib2(n - 1, memoize) + getNthFib2(n - 2, memoize)
        return memoize[n]


# O(N) T O(1) S
def getNthFib3(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        lastTwo[0], lastTwo[1] = lastTwo[1], lastTwo[0] + lastTwo[1]
        counter += 1
    return lastTwo[1]
