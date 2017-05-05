import sys

if sys.platform  != 'win32':
	torrent_dir = '/temp'
else:
	torrent_dir = 'd:\\temp\\'

url = 'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt'
