def solution(s):

    print('\n', s)

    # max size of string
    HALLWAY_SIZE = len(s)

    # convert walks to right or left in two different lists
    right_walkers = []
    left_walkers = []
    for i in range(0, HALLWAY_SIZE):
        if s[i] == '>':
            right_walkers.append(1)
            left_walkers.append(0)
        elif s[i] == '<':
            left_walkers.append(1)
            right_walkers.append(0)
        else:
            right_walkers.append(0)
            left_walkers.append(0)

    print(f'right_walkers: {right_walkers}')
    print(f'left_walkers: {left_walkers}')

    # sum the amount of 'encounters' that right-walking minions will have
    amount_encounters_left2right = 0
    for i in range(0, HALLWAY_SIZE):
        if right_walkers[i] == 1:
            amount_encounters_left2right += sum(left_walkers[i:HALLWAY_SIZE]) 
    print(f'Contagem esbarroes direita: {amount_encounters_left2right}')

    # sum the amount of 'encounters' that left-walking minions will have
    amount_encounters_right2left = 0
    for i in reversed(range(0, HALLWAY_SIZE)):
        if left_walkers[i] == 1:
            amount_encounters_right2left += sum(right_walkers[0:i]) 
    print(f'Contagem esbarroes esquerda: {amount_encounters_right2left}')

    return amount_encounters_left2right + amount_encounters_right2left
                

assert solution('>----<') == 2
assert solution('<<>><') == 4
assert solution('--->-><-><-->-') == 10