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

    print(right_commands)
    print(left_commands)


    contagem_esbarroes_direita = 0
    for i in range(0, HALLWAY_SIZE):
        if right_commands[i] == '>':
            for j in range(i, HALLWAY_SIZE):
                if left_commands[i] == '<':
                    contagem_esbarroes_direita = contagem_esbarroes_direita + 1            
    print(f'Contagem esbarroes direita: {contagem_esbarroes_direita}')
                

solution('>----<')
solution('<<>><')