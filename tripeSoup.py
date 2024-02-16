from bs4 import BeautifulSoup
from lxml import etree 
from requests import get

def get_song_text_and_chords_bg(url):
    page = get(url)
    page.encoding = 'utf-8'
    tripe_soup = BeautifulSoup(page.text, 'html.parser')

    song_title_and_artist = tripe_soup.find(id = 'SongHeader' ).text
    song = tripe_soup.find('div', class_ = 'Song').text

    return(song_title_and_artist + song)

def get_song_text_and_chords_en(source):
    tripe_soup = BeautifulSoup(source, 'html.parser')

    song_title_and_artist = tripe_soup.find(class_='ryCTx FiAaP').text
    song = tripe_soup.find(class_ = 'P8ReX').text
    return (song_title_and_artist + '\n' + '\n' + song)