from instaloader import Profile,Instaloader
from time import sleep
import getpass
import sqlite3
from datetime import datetime




# instância do Instaloader

# dirname_pattern='foto' > para salvar a foto na pasta (fotos)
L = Instaloader(dirname_pattern='fotos')

# loop
while True:

    print(''' ========== INSTAGRAM INFO ==========
[1] - INFORMAÇÕES DO PERFIL  (COM LOGIN)
[2] - INFORMAÇÕES DO PERFIL  (SEM LOGIN)
[3] - COMPARAR MUNDANÇAS DO PERFIL 
[4] - SAIR DO PROGRAMAR..
===============  FSX     =============

''')
    opecion = int(input('Escolha uma opção:'))
    
    # opção 1
    if opecion == 1:
        print('FAÇA O LOGIN..')
        USER = str(input('NOME DE USÚARIO: ')).strip().lower()
        
        # salvando login
        try:
            L.load_session_from_file(USER)
            print(f'Bem-vindo,{USER}!')
    
        except FileNotFoundError:
            print('Erro: Não foi possível encontrar o login.')
            PASS = getpass.getpass('SENHA: ').strip()
            L.login(USER,PASS)
            L.save_session_to_file()

    # MENU
        print(''' ========== INSTAGRAM INFO ==========
        [1] - INFORMAÇÕES DO PERFIL
        [2] - BAIXAR FOTO DO PERFIL
        [3] - SAIR DO PROGRAMAR..
        
        ''')
        
        opecion = int(input('Escolha uma opção:'))
        
    # FUNCIONANDO
        if opecion == 1:
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
            continue
        
        elif opecion == 2:
            ALVO = input('NOME DO ALVO:')
            perfil = Profile.from_username(L.context,ALVO)

            L.download_profile(ALVO,profile_pic_only=True)
            print('DOWNLOAD CONCLUÍDO! ')
            continue

        elif opecion == 3: 
            print('Saindo...')
            continue
    
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
        continue
    
    
    if opecion == 3:

        con = sqlite3.connect('instagram.progre...')
    
        cur = con.cursor()
    

        cur.execute(''' CREATE TABLE IF NOT EXISTS perfil(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        seguidores INTEGER,
        seguindo INTEGER,
        num_posts INTEGER,
        foto_perfil TEXT,
        data_coleta TEXT
        )

        ''')
        con.commiti()
    
    
    
    
    
    
    
    
    
    
    
    # opção 4  
    if opecion == 4:
        print('Saindo...')
        break
    
print('FIM DO PROGRAMAR...')    