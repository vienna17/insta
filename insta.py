from instaloader import Profile,Instaloader
from time import sleep



# instância do Instaloader
L = Instaloader()
# loop
while True:

    print(''' ========== INSTAGRAM INFO ==========
[1] - Informações de um perfil (completa)
[2] - Informações de um perfil (resumida)
[3] - Sair do programar.
===============  FSX     =============

''')
    opecion = int(input('Escolha uma opção:'))
    # opção 1
    if opecion == 1:
        USER = str(input('nome de usuário:')).strip().lower()
        PASS = str(input('senha:'))

        L.login(USER,PASS)
        print('logado com sucesso!')

    # carregar o perfil; todas as informações ; buscar os seguidores...
    
    else:
        pass
    
    # opção 2
    if opecion == 2:
        USERNAME = str(input('nome do usuário alvo: ')).strip().lower()
        profile = Profile.from_username(L.context, USERNAME)
        ID = profile.userid

    # get_info
        BIO = profile.biography
        FOLLOWERS = profile.followers
        FOLLOWING = profile.followees
        POSTS = profile.mediacount
        PRIVATE = profile.is_private
        URL = profile.get_profile_pic_url()

    # print_info
        sleep(2)
        print(
        '\nID:',ID,
        '\nURL:',URL,
        '\nPRIVATE:',PRIVATE,
        '\nBIO:',BIO,
        '\nFOLLOWERS:',FOLLOWERS,
        '\nFOLLOWING:',FOLLOWING,
        '\nPOSTS:',POSTS
        )
    # opção 3   
    if opecion == 3:
        print('Saindo...')
        break
    
print('Fim do programar...')    