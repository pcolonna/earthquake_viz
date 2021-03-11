import requests
import config

def build():
	"""Code to build the whole dataset"""


def get_data():
	url = config.base_url
	r = requests.get(url)

	print(r.json())

if __name__ == '__main__':
	get_data()