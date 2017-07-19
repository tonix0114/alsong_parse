import requests
import HTMLParser

"""
python 3.4 Version or later
import html
def unescape(data):
	return html.unescape(data)

python 3.3 Version or below
import html.parser
def unescape(data):
	parser = html.parser.HTMLParser()
	return parser.unescape(data)
"""
# For python 2.7
def unescape(data):
	parser = HTMLParser.HTMLParser()
	return parser.unescape(data)

def get_tag(xml, tag_start , tag_end):
	start = xml.find(tag_start)
	end = xml.find(tag_end)
	if start == -1 or end == -1:
		return [-1, -1] # error
	return xml[start+len(tag_start):end], end + len(tag_end)
	
def get_song_blocks(xml):
	signature = "ST_GET_RESEMBLELYRIC2_RETURN"
	song_blocks = []
	while xml.find(signature) != -1:
		start = "<" + signature + ">"
		end = "</" + signature + ">"
		tag, idx = get_tag(xml, start, end)
		song_blocks.append(tag)
		xml = xml[idx:]
	return song_blocks

def get_song(xml, tag_keywords):
	tag_blocks = get_song_blocks(xml)
	song_list = []
	while tag_blocks:
		tag_block = tag_blocks.pop(0)
		song = {}
		for keyword in tag_keywords:
			start = "<" + tag_keywords[keyword] + ">"
			end = "</" + tag_keywords[keyword] + ">"
			tag, idx = get_tag(tag_block, start, end)
			if tag == -1:
				continue	
			if tag_keywords[keyword] == "strLyric":
				song[keyword] = tag.split("<br>")[:-1]
			else:
				song[keyword] = tag
		song_list.append(song)
	return song_list

def parse(title, artist, tag_keywords={"id":"strInfoID"}):
	url = "http://lyrics.alsong.co.kr/alsongwebservice/service1.asmx"
	xml = '<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope" xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns2="ALSongWebServer/Service1Soap" xmlns:ns1="ALSongWebServer" xmlns:ns3="ALSongWebServer/Service1Soap12"><SOAP-ENV:Body><ns1:GetResembleLyric2><ns1:stQuery><ns1:strTitle>' + title + "</ns1:strTitle><ns1:strArtistName>" + artist + "</ns1:strArtistName><ns1:nCurPage>0</ns1:nCurPage></ns1:stQuery></ns1:GetResembleLyric2></SOAP-ENV:Body></SOAP-ENV:Envelope>"
	sess = requests.Session()
	sess.headers.update({"Content-Type" : "text/xml;charset=utf-8"})
	return get_song(unescape(sess.post(url, data=xml).text), tag_keywords)
	
	
