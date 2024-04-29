t = int(input())

for i in range(1, t + 1):
    shel, raj = input().split()
    if shel == raj:
        print(f'Caso #{i}: De novo!')
    else:
        if (shel == 'tesoura') and (raj != 'Spock') and (raj!= 'pedra'):
            print(f'Caso #{i}: Bazinga!')
        elif (shel == 'papel') and (raj != 'lagarto') and (raj!= 'tesoura'):
            print(f'Caso #{i}: Bazinga!')
        elif (shel == 'pedra') and (raj != 'papel') and (raj!= 'Spock'):
            print(f'Caso #{i}: Bazinga!')
        elif (shel == 'lagarto') and (raj != 'pedra') and (raj!= 'tesoura'):
            print(f'Caso #{i}: Bazinga!')
        elif (shel == 'Spock') and (raj != 'lagarto') and (raj!= 'papel'):
            print(f'Caso #{i}: Bazinga!')
        else:
            print(f'Caso #{i}: Raj trapaceou!')