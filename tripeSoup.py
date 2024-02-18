from bs4 import BeautifulSoup
from requests import get
from selenium.common.exceptions import NoSuchElementException

def get_song_text_and_chords_bg(url):
    page = get(url)
    page.encoding = 'utf-8'
    tripe_soup = BeautifulSoup(page.text, 'html.parser')

    song_title_and_artist = tripe_soup.find(id='SongHeader')
    if song_title_and_artist == None:
        raise NoSuchElementException
    
    song_title_and_artist = song_title_and_artist.text
    song = tripe_soup.find('div', class_='Song').text

    return song_title_and_artist + song

def get_song_text_and_chords_en(source):
    tripe_soup = BeautifulSoup(source, 'html.parser')

    song_title_and_artist = tripe_soup.find(class_='ryCTx FiAaP')
    if song_title_and_artist == None:
        raise NoSuchElementException
    song_title_and_artist = song_title_and_artist.text
    song = tripe_soup.find(class_ = 'P8ReX').text
    return (song_title_and_artist + '\n' + '\n' + song)