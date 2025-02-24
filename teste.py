from instaloader import Profile, Instaloader
import time

L = Instaloader(dirname_pattern='fotos')

USERNAME = str(input('NOME DO USÚARIO: '))
PASSWORD = input('SENHA: ')

L.login(USERNAME,PASSWORD)
print('LOGADO COM SUCESSO..')

alvo = input('ALVO: ')
perfil = Profile.from_username(L.context,alvo)

L.download_profile(alvo,profile_pic_only=True)
print('Download concluído!')

