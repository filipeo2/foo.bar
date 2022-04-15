def solution(n):
    num = int(n)
    print('\n', num)

    from bisect import bisect_left

    # 1030 positions is enough to generate all the power of 2 possibilities that reaches 309 characters long
    lista = [2 ** i for i in range(1030)]

    #print(len(str(lista[-1])))
    #print((lista[-1]))

    # get closest index of n in the previous list (stops at next if not exists)
    position = bisect_left(lista, num)
    print(f'position: {position} lista[]: {lista[position]}')

    # 0 is positive but does not exists in our list and costs 1 add_operation
    if num in [0]:
        return 1
   
    # check the current index, if is a match
    steps_to_closest = 0
    if num == lista[position]:
        print(f'Achou!')
        pass

    # if the previous index is the closest, consider it as the base position (-1) and calculates how many add_operations are necessary
    elif num - lista[position - 1] <= lista[position] - num:
        steps_to_closest = num - lista[position - 1]
        print(f'previous is the closest: {lista[position - 1]}, steps to the closest: {steps_to_closest}')
        position -= 1

    # if the next index is the closest, consider it as the base position and calculates how many remove_operations are necessary
    else:
        steps_to_closest = lista[position] - num
        print(f'next is the closest: {lista[position]}, steps to the closes: {steps_to_closest}')
        
    result = position + steps_to_closest
    print(f'Result: {result}')
    return result

assert solution('0') == 1
assert solution('1') == 0
assert solution('2') == 1
assert solution('3') == 2
assert solution('4') == 2
assert solution('15') == 5