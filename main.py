#-*- coding:euc-kr -*-
import alsong
import xml.dom.minidom as xdom
import sys

def main():
	tag_keywords = {"id":"strInfoID","title":"strTitle", "artist":"strArtistName", "album":"strAlbumName", "text":"strLyric"}
	if len(sys.argv) > 2:
		title = sys.argv[1]
		artist = sys.argv[2]
		songs = alsong.parse(title, artist, tag_keywords)
		for song in songs:
			for t in song["text"]:
				print t
				exit()
	else:
		print "input sjgdjdy"
if __name__ == '__main__':
	main()
