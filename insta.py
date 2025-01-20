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
        
        try:
            L.load_session_from_file(USER)
            print(f'Ben-vindo,{USER}!')
    
        except FileNotFoundError:
            print('Erro: Não foi possível encontrar o login.')

            PASS = str(input('senha:')).strip()
            L.login(USER,PASS)
            L.save_session_to_file()

    # MENU
        print(''' ========== INSTAGRAM INFO ==========
        [1] - listar seguidores
        [2] - Informações do perfil 
        [3] - Sair do programar
        
        ''')
        opecion = int(input('Escolha uma opção:'))

        #if opecion == 1:
        
    # FUNCIONANDO
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
            '\nPOSTS:',POSTS)
        
        
        
        #else: 
           # print('Saindo...')
            #break
    
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