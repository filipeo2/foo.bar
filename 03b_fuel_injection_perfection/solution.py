def solution(n):
    print('\n', n)

    from bisect import bisect_left

    # 1030 positions is enough to generate all the power of 2 possibilities that reaches 309 characters long
    lista = [2 ** i for i in range(1030)]

    #print(len(str(lista[-1])))
    #print((lista[-1]))

    # get closest index of n in the previous list (stops at next if not exists)
    position = bisect_left(lista, n)
    print(f'position: {position} lista[]: {lista[position]}')

    # 0 is positive but does not exists in our list and costs 1 add_operation
    if n in [0]:
        return 1
   
    # check the current index, if is a match or what position is the closest: previous or next
    steps_to_previous = steps_to_next = 0
    if n == lista[position]:
        print(f'Achou!')
        pass

    # if the previous index is closest, consider it as the base position and calculates how many add_operations are necessary
    elif n - lista[position - 1] <= lista[position] - n:
        steps_to_previous = n - lista[position - 1]
        print(f'previous is the closest: {lista[position - 1]}, steps to the closest: {steps_to_previous}')
        position -= 1

    else:
        steps_to_next = lista[position] - n
        print(f'next is the closest: {lista[position]}, steps to the closes: {steps_to_next}')
        
    resultado = position + steps_to_next + steps_to_previous
    print(f'Resultado: {resultado}')
    return resultado

assert solution(0) == 1
assert solution(1) == 0
assert solution(2) == 1
assert solution(3) == 2
assert solution(4) == 2
assert solution(15) == 5