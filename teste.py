import instaloader
import time

# Inicializa o Instaloader
L = instaloader.Instaloader()

# Login no Instagram
USE = input('Nome do usuário: ').strip()
PASS = input('Senha: ').strip()

try:
    L.login(USE, PASS)
    print('Logado com sucesso!')
except instaloader.exceptions.BadCredentialsException:
    print("Erro: Nome de usuário ou senha incorretos.")
    exit()
except instaloader.exceptions.TwoFactorAuthRequiredException:
    print("Erro: Autenticação de dois fatores necessária.")
    exit()
except Exception as e:
    print(f"Erro inesperado: {e}")
    exit()

# Obtém informações do alvo
alvo = input('Nome do alvo: ').strip()
try:
    profile = instaloader.Profile.from_username(L.context, alvo)
    print(f"Coletando seguidores de: {alvo}")
except instaloader.exceptions.ProfileNotExistsException:
    print(f"Erro: O perfil '{alvo}' não existe.")
    exit()
except Exception as e:
    print(f"Erro inesperado ao acessar o perfil: {e}")
    exit()

# Obtém seguidores com controle de exceções
try:
    seguidores = profile.get_followers()
    for seguidor in seguidores:
        print(seguidor.username)
        time.sleep(1)  # Aguarda 1 segundo entre as requisições para evitar bloqueios
except instaloader.exceptions.ConnectionException as e:
    print(f"Erro de conexão: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
