import requests

from config import url

def get_page_source(url = url):
	r = requests.get(url)
	if r.status_code != 200:
		raise ConnectionError
		return
	return r.text

def set_list(source = get_page_source()):
	lst = []
	for url in source.split('\n'):
		if url != '':
			#print(url)
			lst.append(url)
	return lst

def get_list():
	return set_list()

if __name__ == '__main__':
	set_list()