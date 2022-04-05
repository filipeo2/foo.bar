from collections import Counter

def solution(data, n):
    
    #generates a counter collection and remove items greater than N
    lista_counter = Counter(data)
    lista_ordenada = [k for k, v in lista_counter.items() if v <= n]

    # define the final list in the exact original order
    lista_final = []
    for i in data:
        if i in lista_ordenada:
            lista_final.append(i)
    
    return lista_final

# print(solution2([5, 10, 15, 10, 7], 1))
assert solution([5, 10, 15, 10, 7], 1) == [5, 15, 7]
solution([0,1,2,2,3,5,5,5,5], 1)
solution([0,1,2,2,3,5,5,5,5], 2)
solution([1,2,2,-5,5,-5,5], 1)
solution([1,2,2,-5,5,-5,5], -1)
solution([1,2,2,5,5,5,99], 2)
solution([1,7,2,9,9,5,99,99,99], 2)