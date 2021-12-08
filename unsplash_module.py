import requests
#pics = requests.get('https://api.unsplash.com/photos/random?client_id=')
#pics=pics.json()
#print(pics["urls"]["raw"])

class UnsplashClass:
	def __init__(self):
		self.pics=requests.get('https://api.unsplash.com/photos/random?client_id=')
		self.pics = self.pics.json()
		#print(self.pics)
		self.url = self.pics["urls"]["raw"]
