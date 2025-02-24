from instaloader import Profile, Instaloader
import time

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
    nu = int(input('QUANTAS FOTOS VOCÊ DESEJA BAIXAR? '))

    for index,post in enumerate(perfil.get_posts()):
        if index >= nu:
            break
        print(f'BAIXANDO FOTOS {index + 1}..')
        L.download_post(post,target=perfil.username)
        time.sleep(2)

    print('DOWNLOADER CONCLUIDO! ')

if opção == 'n':
    print('Operação cancelada.')


# FAZER UM INPUT PARA O USÚARIO ESCOLHER QUANTAS FOTOS QUER BAIXAR