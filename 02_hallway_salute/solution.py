def solution(s):
    print('\n', s)

    HALLWAY_SIZE = len(s)

    right_commands = []
    left_commands = []
    for i in range(0, HALLWAY_SIZE):
        if s[i] == '>':
            right_commands.append(s[i])
            left_commands.append(' ')
        elif s[i] == '<':
            left_commands.append(s[i])
            right_commands.append(' ')
        else:
            right_commands.append(' ')
            left_commands.append(' ')

    print(f'right_commands: {right_commands}')
    print(f'left_commands: {left_commands}')

    # encounters from left to right
    contagem_esbarroes_direita = 0
    for i in range(0, HALLWAY_SIZE):
        if right_commands[i] == '>':
            for j in range(i, HALLWAY_SIZE):
                if left_commands[j] == '<':
                    contagem_esbarroes_direita += 1            
    print(f'Contagem esbarroes direita: {contagem_esbarroes_direita}')
                

    # encounters from right to left
    contagem_esbarroes_esquerda = 0
    for i in reversed(range(0, HALLWAY_SIZE)):
        # print('i', i)
        if left_commands[i] == '<':
            # print(left_commands[i])
            for j in reversed(range(0, i)):
                if right_commands[j] == '>':
                    # print(right_commands[j])
                    contagem_esbarroes_esquerda += 1            
    print(f'Contagem esbarroes esquerda: {contagem_esbarroes_esquerda}')

    return contagem_esbarroes_direita + contagem_esbarroes_esquerda
                

assert solution('>----<') == 2
assert solution('<<>><') == 4
assert solution('--->-><-><-->-') == 10