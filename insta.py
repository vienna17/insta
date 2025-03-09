from instaloader import Profile,Instaloader
from time import sleep
import getpass
import sqlite3
from datetime import datetime
import bcrypt




# instância do Instaloader

# dirname_pattern='foto' > para salvar a foto na pasta (fotos)
L = Instaloader(dirname_pattern='fotos')

# loop
while True:

    print(''' ========== INSTAGRAM INFO ==========
[1] - INFORMAÇÕES DO PERFIL  (COM LOGIN)
[2] - INFORMAÇÕES DO PERFIL  (SEM LOGIN)
[3] - SALVA DADOS DO PERFIL PARA COMPARAR MUNDANÇAS 
[4] - SAIR DO PROGRAMAR..
===============  FSX     =============

''')
    opecion = int(input('ESCOLHA UMA OPÇÃO:'))
    
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
        [3] - VOLTAR..
        
        ''')
        
        opecion = int(input('ESCOLHA UMA OPÇÃO:'))
        
    # FUNCIONANDO
        if opecion == 1:
            USERNAME = str(input('NOME DO ALVO: ')).strip().lower()
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
        USERNAME = str(input('NOME DO ALVO: ')).strip().lower()
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

        con = sqlite3.connect('Banco_de_dados')
    
        cur = con.cursor()
    

        cur.execute(''' CREATE TABLE IF NOT EXISTS perfil(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        seguidores INTEGER,
        seguindo INTEGER,
        num_posts INTEGER,
        foto_perfil TEXT,
        bio TEXT,
        private INTEGER,
        data_coleta TEXT
        )

        ''')
        con.commit()

        # Dados do perfil 

        L = Instaloader()

        novoperfil= input('NOME DO PERFIL ALVO: ').strip()
        profile = Profile.from_username(L.context,novoperfil)
    
        bio = profile.biography if profile.biography else ""
        seguidores = profile.followers
        seguindo = profile.followees
        posts = profile.mediacount
        private = profile.is_private
        foto = profile.profile_pic_url
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        cur.execute('SELECT seguidores,seguindo,num_posts,bio,foto_perfil,private FROM perfil WHERE username = ?',(novoperfil,))
        ultimo_registro = cur.fetchone()


        if ultimo_registro:
          
            ult_seguidores, ult_seguindo, ult_posts, ult_bio, ult_foto, ult_private = ultimo_registro


            print('COMPARANDO O PERFIL: ')
            if ult_seguidores != seguidores:
                print(f'SEGUIDORES: {ult_seguidores} > {seguidores}')
            if ult_seguindo != seguindo:
                print(f'SEGUINDO: {ult_seguindo} > {seguindo}')
            if ult_posts != posts:
                print(f'POSTS: {ult_posts} > {posts}')
            if ult_bio != bio:
                print(f'BIO: {ult_bio} > {bio}')
            if ult_private != private:
                print(f'PRIVADO: {ult_private} > {private}')
            if ult_foto != foto:
                print(f'FOTO ANTIGA: {ult_foto} FOTO ATUAL {foto}')

        else:
            cur.execute('''
            INSERT INTO perfil (username,seguidores,seguindo,num_posts,foto_perfil,private,data_coleta)
            VALUES (?,?,?,?,?,?,?)''',
            (novoperfil,seguidores,seguindo,posts,foto,private,data_atual))
            con.commit()
            print(f"NOVO PERFIL SALVO NO BANCO DE DADOS! ")
        
        con.close()














    
    # opção 4  
    if opecion == 4:
        print('Saindo...')
        break
    
print('FIM DO PROGRAMAR...')    