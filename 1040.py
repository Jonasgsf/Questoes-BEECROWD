n1,n2,n3,n4 = list(map(float, input().split()))
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4)) / 10
if media >= 7:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
else:
    if media < 5:
        print(f'Media: {media:.1f}')
        print('Aluno reprovado.')
    else:
        print(f'Media: {media:.1f}')
        print('Aluno em exame.')
        nexame = float(input())
        notafinal = ((nexame + media) / 2)
        if notafinal >= 5:
            print(f'Nota do exame: {nexame:.1f}')
            print('Aluno aprovado.')
            print(f'Media final: {notafinal:.1f}')
        else:
            print('Aluno reprovado.')
            print(f'Media final: {notafinal:.1f}')
