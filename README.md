# InstaChord
 
Python project for the Introduction to Python Programming course @ FMI. The basic idea is that you're looking for the chords and text of a song and InstaChord deliver them to you in a way that the chords are synchronized with the text so that you can play the chords and sing at the same time. In the project im using BeautifulSoup and Selenium for webscraping, customTkinter for the GUI, Shazam and Youtube APIs, SQLAlchemy for the database part and kind of a Shazam API for immediate song recognition.

Screenshots fom the app:

-Main screen:
![main_screen](https://github.com/momouzunov2003/InstaChord/assets/115097765/6c2cf25a-c1cd-4a32-91af-3955760f8567)
-Searching for an artist:
![artist1](https://github.com/momouzunov2003/InstaChord/assets/115097765/a50ea6c5-fbc7-4e80-9171-1219f955d6b9)
![artist2](https://github.com/momouzunov2003/InstaChord/assets/115097765/2a751c4b-92c5-4d22-b787-abdbbd522578)
![artist_result](https://github.com/momouzunov2003/InstaChord/assets/115097765/20964a4c-6b4b-47f4-8c1a-b60366193d24)
-Searching for an exact song:
![song1](https://github.com/momouzunov2003/InstaChord/assets/115097765/cef3669b-e97d-47ca-8040-0ec0ad50af3e)
![songbg](https://github.com/momouzunov2003/InstaChord/assets/115097765/266aaebb-09ee-423e-86e3-66ed99613932)
-Uploading a song:
![upload_song](https://github.com/momouzunov2003/InstaChord/assets/115097765/0ac6b82b-1838-4c71-857f-52814d10cd5a)
![upload_result](https://github.com/momouzunov2003/InstaChord/assets/115097765/950d4f0c-50d1-415f-a87c-7b8bdb00bf20)



DISCLAIMER: When searching for a bulgarian song the input string is case sensitive(only the first letter of the song's name, a month's name or a person's name should be capital). For using the song recognition function the songs must be in .mp3 format!
