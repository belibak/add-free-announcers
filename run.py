#!/usr/bin/env python3
import encode
import argparse
import os
import sys

from config import torrent_dir
from getlist import get_list

if sys.platform != 'win32':
	edited_dir = torrent_dir + 'announcers_added/'
else:
	edited_dir = torrent_dir + 'announcers_added\\'

if os.path.exists(edited_dir):
		pass
else:
	os.mkdir(edited_dir)

def find_torrents(dir = torrent_dir):
	files = [i for i in os.listdir(dir) if i[-7:] == 'torrent']
	return files

def args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', help = "--search", default = False)
	params = parser.parse_args()
	return params


filenames = find_torrents()


def add_announcers(filename, dir = torrent_dir):
	with open(dir + filename, 'rb') as file:
		tdb = file.read()
		other = encode.bdecode(tdb)
		dct = other
		try:
			ann_list = dct['announce-list']
		except KeyError:
			ann_list = []

	announcers = get_list()

	for announcer in announcers:
		tl = []
		tl.append(announcer)
		ann_list.append(tl)

	dct['announce-list'] = ann_list

	pack_back = encode.bencode(dct)


	with open(edited_dir + filename, 'wb') as file:
		file.write(pack_back)
		print('%s saved to %s' %(filename, edited_dir))
	file.close()

if __name__ == "__main__":
	for i in filenames:
		try:
			add_announcers(i)
		except encode.DecodingException:
			print("Decoding exception in file \"" + i + "\"")
	input('Press enter to close window...')
