# -*- coding: utf-8 -*-
# This script will fetch song lyrics from lyricsfreak.com
import urllib.request
from bs4 import BeautifulSoup
import re
from sys import argv

script, song = argv

def find_song(song):
    # Split the words in the song name using spaces
    split_song = song.split(" ")
    # This is the base URL that is always used to search for songs
    s_url = "http://www.lyricsfreak.com/search.php?a=search&type=song&q="

    # Variable 'x' is used in the for loop to build the URL
    x = 0
    # For every word in the song name...
    for i in split_song:
        # Add the word to the base search URL
        s_url = s_url + i
        x += 1
        # And add '+' after the word, if this is not the last word
        if x < len(split_song):
            s_url = s_url + "+"

    # Open the URL page into variable 'page'
    page = urllib.request.urlopen(s_url)
    # Transfer the data into a string, decode it, and store into var 'data'
    data = (page.read().strip().decode('utf-8'))
    # Split the html page into separate lines
    line = data.splitlines()
    # For every line in the html page...
    for i in line:
        # Check if part of the name of the song exists in a line
        if split_song[0] in i:
            # If it does, store that line in a variable
            line = i
    # Split the lines using '"' as the splitter
    line = line.split('"')
    # Add the part that has the song name to the base URL
    link = "http://www.lyricsfreak.com" + line[1]
    # Now we have the page that contains the lyrics and we will modify that
    # Fetch the page in html and store into variable 'page'
    page = urllib.request.urlopen(link)
    # transfer the html data into a string and store into variable 'data'
    data = (page.read().strip().decode('utf-8'))
    # separate song lyrics form the rest of the html page
    data = data.split("<!-- SONG LYRICS -->")
    data = data[1].split("<!-- /SONG LYRICS -->")
    # parse the lyrics to readable form
    lyrics = BeautifulSoup(data[0], "lxml")
    lyrics = lyrics.decode("unicode-escape")
    lyrics = re.sub('<[^<]+?>', '', lyrics)
    lyrics = re.sub('\n\n', '', lyrics)
    print(lyrics)

find_song(song)