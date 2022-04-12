

def solution(l):
    import itertools
    # print('\n', l)

    # generates all possible combination with length 3
    possible_combinations = itertools.combinations(l, 3)

    # check if each combination meets the requirements
    lucky_triples_amount = 0
    for (x, y, z) in possible_combinations:
        if x <= y and y <= z and z % y == 0 and y % x == 0: 
            print(x, y, z)
            lucky_triples_amount += 1

    return lucky_triples_amount

def solution2(l):
    from itertools import product

    print('\n', l)
    
    resultado = 0
    for i in range(0, len(l)):
        mult_menor = [l[x] for x in range(0, i) if l[x] <= l[i] and l[i] % l[x] == 0]
        mult_maior = [l[x] for x in range(i+1, len(l)) if l[i] <= l[x] and l[x] % l[i] == 0]
        # print(f'{l[i]}|{mult_menor} {mult_maior}')

        if len(mult_menor) > 0 and len(mult_maior) > 0:
            # print(list(product(mult_menor, mult_maior)))
            resultado += len(list(product(mult_menor, mult_maior)))
    
    print(resultado)
    return resultado
    

# print('Resultado: ', solution2([1, 2, 3, 4, 5, 6]))
assert solution2([1, 2, 3, 4, 5, 6]) == 3
assert solution2([1, 1, 1]) == 1
assert solution2([1, 2, 5]) == 0
assert solution2([111111, 333333, 666666, 999999]) == 2
assert solution2([]) == 0
assert solution2([1, 1, 1, 1, 1]) == 1
