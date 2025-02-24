from instaloader import Profile, Instaloader

L = Instaloader(dirname_pattern='fotos')

USERNAME = str(input('NOME DO USÚARIO: '))
PASSWORD = input('SENHA: ')

L.login(USERNAME,PASSWORD)
print('LOGADO COM SUCESSO..')

# PEGAR O NÚMERO DE POSTS DO USÚARIO 
while True:
    print('INSIRA O NOME DO ALVO PARA VER A QUANTIDADE DE FOTOS')
    alvo = input('ALVO: ')
    perfil = Profile.from_username(L.context,alvo)
    
    POSTS = perfil.mediacount

    print('O NÚMERO DE POSTS DO USÚARIO É',POSTS)
    break
print('DESEJA BAIXAR ALGUM POST DO ALVO? ')

opção = str(input('S/N: ')).lower()

if opção == 's':
    # BAIXAR POST
    print('EM MANUTENÇÃO...')

if opção == 'n':
    print('Operação cancelada.')


# FAZER UM INPUT PARA O USÚARIO ESCOLHER QUANTAS FOTOS QUER BAIXAR