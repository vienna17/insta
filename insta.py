import instaloader
from time import sleep

# instância do Instaloader
L = instaloader.Instaloader()

# login (opcional)

login = str(input('deseja fazer login? [s/n]:'))
sleep(2)
if login == 's':
    USER = str(input('nome de usuário:'))
    PASS = str(input('senha:'))
    L.login(USER,PASS)
else:
    pass

# get_profile
USERNAME = str(input('nome do usuário alvo: ')).lower()
profile = instaloader.Profile.from_username(L.context, USERNAME)
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
