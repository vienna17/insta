from instaloader import Instaloader,Profile
import json

L = Instaloader()
USERNAME = input('usuario')
PASSWORD = input('senha')
L.login(USERNAME,PASSWORD)
profile = Profile.from_username(L.context,USERNAME)

get_s = profile.get_followers()

for seguidor in get_s:
    print(seguidor.username)