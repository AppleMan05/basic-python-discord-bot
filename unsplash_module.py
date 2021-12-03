import requests
#pics = requests.get('https://api.unsplash.com/photos/random?client_id=tM2L0PhCLzxWirzY3W7hDnsaNeX3WHJm30Civ4DA5Jo')
#pics=pics.json()
#print(pics["urls"]["raw"])

class UnsplashClass:
        def __init__(self):
                self.pics = requests.get('https://api.unsplash.com/photos/random?client_id=').json()
        url = pics["urls"]["raw"]
    