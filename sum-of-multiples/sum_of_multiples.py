def sum_of_multiples(limit, multiples_list):
    if not multiples_list:
        return 0

    unique_factors = get_unique_factors(multiples_list)
    test_nums = range(unique_factors[0], limit)
    multiples = [n for n in test_nums if is_multiple(n, unique_factors)]

    return sum(multiples)

def get_unique_factors(multiples_list):
    test_factors = multiples_list
    unique_factors = [test_factors.pop(0)]

    while test_factors:
        n = test_factors.pop(0)
        if not is_multiple(n, unique_factors):
            unique_factors.append(n)

    return unique_factors

def is_multiple(n, multiples_list):
    for m in multiples_list:
        if n % m == 0:
            return True
    return False
