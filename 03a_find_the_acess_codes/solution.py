def solution(l):
    import itertools
    print('\n', l)

    # generate all possible combination with lenght 3
    possible_combination = itertools.combinations(l, 3)

    # check if each combination meets the requirements
    lucky_triples_amount = 0
    for combination in possible_combination:
        if combination[1] % combination[0] == 0 and combination[2] % combination[1] == 0:
            # print(combination)
            lucky_triples_amount += 1

    return lucky_triples_amount


# print('Resultado: ', solution([1, 2, 3, 4, 5, 6]))

assert solution([1, 2, 3, 4, 5, 6]) == 3
assert solution([1, 1, 1]) == 1