from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Song(Base):
    __tablename__ = "Name and lyrics"

    song_title = Column("Title", String, primary_key=True)
    lyrics_and_chords = Column("Lyrics", String)

    def __init__(self, title, lyrics):
        self.song_title = title
        self.lyrics_and_chords = lyrics

    def __repr__(self):
        return f"{self.song_title} '\n' {self.lyrics_and_chords}" 
    

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_song_to_db(title, text):
    song = Song(title=title, lyrics=text)
    session.add(song)
    session.commit()

def get_song_from_db(title):
    lyrics = session.query(Song.lyrics_and_chords).filter(Song.song_title == title)
    return lyrics