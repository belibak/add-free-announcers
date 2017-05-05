import sys

if sys.platform  != 'win32':
	# for linux users
	torrent_dir = '/tmp/'
else:
	# for windows users
	torrent_dir = 'd:\\temp\\'

url = 'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt'
