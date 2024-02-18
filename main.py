import gui
import spotifyAPI
import webcrawling
import helpers
import tripeSoup
import shazam
import selenium
import database
import youtubeAPI

def artist_button_push():
    for widget in gui.central_frame.winfo_children():
        widget.destroy()

    artist = gui.search_textbox.get()
    this_artist_id = spotifyAPI.get_artist_id(spotifyAPI.token, artist)
    gui.search_textbox.delete(0,gui.tkinter.END)
    songs_array = spotifyAPI.get_artist_top_tracks(spotifyAPI.token, this_artist_id)

    top_songs = gui.customtkinter.CTkLabel(gui.central_frame, font=(None,24), text="")
    array_text = '\n'.join(_ for _ in songs_array)
    top_songs.configure(text=array_text)
    top_songs.pack(expand=True)

    choice_combobox = gui.customtkinter.CTkComboBox(gui.central_frame, values=songs_array)
    choice_combobox.pack(pady=5)

    choice_button = gui.customtkinter.CTkButton(gui.central_frame, text="Choose")
    choice_button.pack(pady=10)
    
    def choice_button_push():
        first_letter = helpers.find_first_letter_index(choice_combobox.get())
        song_name = choice_combobox.get()[first_letter:]
        search_for_song_main(song_name)

    choice_button.configure(command=choice_button_push)


def search_for_song_main(song_name):
    for widget in gui.central_frame.winfo_children():
        widget.destroy()

    central_frame2 = gui.customtkinter.CTkScrollableFrame(gui.central_frame, fg_color="#383b39")
    central_frame2.pack(fill="both",
                        expand=True,
                        pady=3,
                        padx=3)
    
    song_url = youtubeAPI.get_youtube_link(song_name)
    print(song_url)
    
    if(helpers.is_cyrillic_or_latin(song_name) == "Cyrillic"):
        correct_song_name = song_name[0].upper() + song_name[1:]
        lyrics = database.get_song_from_db(correct_song_name)
        if lyrics.first() is not None:
            print("Song found in DB!")
            text = lyrics[0]
            text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                    text=lyrics[0][0].encode('utf-8').decode('utf-8') + '\n' + 'Youtube link:' + '\n' + song_url,
                                                    text_color='white',
                                                    font=('',15))
            text_label.pack()
        else:
            print("Song not found in DB!")
            try:
                text = (tripeSoup.get_song_text_and_chords_bg(webcrawling.song_bg(song_name)))
                text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                        text=text + '\n' + 'Youtube link:' + '\n' + song_url,
                                                        text_color='white',
                                                        font=('',15))
                text_label.pack()
                database.add_song_to_db(correct_song_name, text)
            except selenium.common.exceptions.NoSuchElementException:
                text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                        text="Song could not be found! Please try again!",
                                                        text_color='white',
                                                        font=('Helvetica',23))
                text_label.pack()           
    elif(helpers.is_cyrillic_or_latin(song_name) == "Latin"):
        correct_song_name = helpers.capitalize_after_space(song_name)
        lyrics = database.get_song_from_db(correct_song_name)
        if lyrics.first() is not None:
            print("Song found in DB!")
            text = lyrics[0]
            text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                    text=lyrics[0][0] + '\n' + 'Youtube link:' + '\n' + song_url,
                                                    text_color='white',
                                                    font=('',15))
            text_label.pack()
        else:
            try:
                text = (tripeSoup.get_song_text_and_chords_en(webcrawling.song_en(song_name)))
                text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                        text=text + '\n' + 'Youtube link:' + '\n' + song_url,
                                                        text_color='white',
                                                        font=('',15))
                text_label.pack()
                database.add_song_to_db(correct_song_name, text)
            except selenium.common.exceptions.NoSuchElementException:
                text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                        text="Song could not be found or there was an error while trying to find it! Please try again!",
                                                        text_color='white',
                                                        font=('Helvetica',23))
                text_label.pack(expand=True)   
            except IndexError:
                text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                        text="Song could not be found or there was an error while trying to find it! Please try again!",
                                                        text_color='white',
                                                        font=('Helvetica',23))
                text_label.pack(expand=True)
            except Exception:
                text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                        text="Song could not be found or there was an error while trying to find it! Please try again!",
                                                        text_color='white',
                                                        font=('Helvetica',23))
                text_label.pack(expand=True)
    else:
        text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                text="Song name doesn't start with a letter! Please try again!",
                                                text_color='white',
                                                font=('Helvetica',23))
        text_label.pack(expand=True)

def song_button_push():
    song_name = gui.search_textbox.get()
    search_for_song_main(song_name)
    

def upload_button_push():
    filetypes = (("Mp3 Files", "*.mp3"),)
    filepath = gui.filedialog.askopenfilename(title="Open a file",
                                              initialdir='/GitHub/InstaChord',
                                              filetypes=filetypes)
                                              
    song_name = shazam.get_song_name(filepath)

    search_for_song_main(song_name)
    

gui.search_song_button.configure(command=song_button_push)
gui.search_artist_button.configure(command=artist_button_push)
gui.upload_button.configure(command=upload_button_push)

gui.root.mainloop()