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
			print song["id"], song["title"], song["artist"]
	else:
		print "input sjgdjdy"
if __name__ == '__main__':
	main()
