def sieve(limit):
    potential_primes = range(2, limit+1)
    primes = []

    while potential_primes:
        # If a number hasn't been filtered out by a previous iteration,
        # it is definitely prime.
        n = potential_primes.pop(0)
        primes.append(n)

        # Filter out all multiples of this number from your list of remaining
        # potential primes. No need to test whether a potential prime is
        # equal to your test number because you've already removed n.
        potential_primes = [c for c in potential_primes if c%n!=0]

    return primes