from lxml import etree
import urllib
import urllib.request

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

with urllib.request.urlopen("http://localhost:8888/search_playlist/?artist=&title=&channel=53&month=&date=&shour=&sampm=&stz=&ehour=&eampm=") as url:
                            s = url.read()

html = etree.HTML(s)

for tbl in html.xpath('//table'):
                            artists = tbl.xpath('.//tr/td[2]/text()')
                            #print("Artists:")
                            #print(artists)
                            songs   = tbl.xpath('.//tr/td[3]/a/text()')
                            #print("Songs:")
                            #print(songs)
                            if artists[1] == "Artist":
                                print("Table successfully parsed.")
                                break

# remove junk entries from beginning of artists table
artists.pop(0)
artists.pop(0)

#remove junk entries from end of artists table
artists.pop()

#remove junk entries from beginning of songs table
songs.pop(0)
songs.pop(0)

#remove junk entries from end of songs table
songs.pop()
songs.pop()

# combine into a dictionary
playlist = dict(zip(artists, songs))

#remove station identification
stationID = playlist.get("@siriusxmchill")
if stationID != None:
    playlist = removekey(playlist, "@siriusxmchill")

#print("Artists: ")
#print(artists)
#print("Songs: ")
#print(songs)

print(playlist)
