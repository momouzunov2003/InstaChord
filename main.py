import gui
import spotifyAPI
import webcrawling
import helpers
import tripeSoup
import shazam

def artist_button_push():
    for widget in gui.central_frame.winfo_children():
        widget.destroy()

    artist = gui.search_textbox.get()
    this_artist_id = spotifyAPI.get_artist_id(spotifyAPI.token, artist)
    gui.search_textbox.delete(0,gui.tkinter.END)
    songs_array = spotifyAPI.get_artist_top_tracks(spotifyAPI.token,this_artist_id)
    #print(songs_array)

    top_songs = gui.customtkinter.CTkLabel(gui.central_frame, font=(None,24),text="")
    array_text = '\n'.join(_ for _ in songs_array)
    top_songs.configure(text=array_text)
    top_songs.pack(expand=True)

    choice_combobox = gui.customtkinter.CTkComboBox(gui.central_frame, values=songs_array)
    choice_combobox.pack(pady=5)

    choice_button = gui.customtkinter.CTkButton(gui.central_frame,text="Choose")
    choice_button.pack(pady=10)
    
    def choice_button_push():
        first_letter = helpers.find_first_letter_index(choice_combobox.get())
        song_name = choice_combobox.get()[first_letter:]
        
        for widget in gui.central_frame.winfo_children():
            widget.destroy()

        central_frame2 = gui.customtkinter.CTkScrollableFrame(gui.central_frame,fg_color="#383b39")
        central_frame2.pack(fill="both",expand=True,pady=3,padx=3)

        if(helpers.is_cyrillic_or_latin(song_name) == "Cyrillic"):
            text = (tripeSoup.get_song_text_and_chords_bg(webcrawling.song_bg(song_name)))
            text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                    text=text,text_color='white',
                                                    font=('',15))
            text_label.pack()
        elif(helpers.is_cyrillic_or_latin(song_name) == "Latin"):
            text2 = tripeSoup.get_song_text_and_chords_en((webcrawling.song_en(song_name)))
            text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                    text=text2,text_color='white',
                                                    font=('',15))
            text_label.pack()
        else:
            print("song name doesn't start with a letter, fix later:D")

    choice_button.configure(command=choice_button_push)


def song_button_push():
    for widget in gui.central_frame.winfo_children():
        widget.destroy()

    central_frame2 = gui.customtkinter.CTkScrollableFrame(gui.central_frame,fg_color="#383b39")
    central_frame2.pack(fill="both",expand=True,pady=3,padx=3)

    song_name = gui.search_textbox.get()

    if(helpers.is_cyrillic_or_latin(song_name) == "Cyrillic"):
        text = (tripeSoup.get_song_text_and_chords_bg(webcrawling.song_bg(song_name)))
        text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                text=text,text_color='white',
                                                font=('',15))
        text_label.pack()
    elif(helpers.is_cyrillic_or_latin(song_name) == "Latin"):
        text2 = tripeSoup.get_song_text_and_chords_en((webcrawling.song_en(song_name)))
        text_label = gui.customtkinter.CTkLabel(central_frame2,
                                                text=text2,text_color='white',
                                                font=('',15))
        text_label.pack()
    else:
        print("song name doesn't start with a letter, fix later:D")

def upload_button_push():
    filetypes=(("Mp3 Files", "*.mp3"),)
    filepath = gui.filedialog.askopenfilename(title="Open a file",
                                              initialdir='/',
                                              filetypes=filetypes)
                                              
    song_name = shazam.get_song_name(filepath)

    if(helpers.is_cyrillic_or_latin(song_name) == "Cyrillic"):
        text = (tripeSoup.get_song_text_and_chords_bg(webcrawling.song_bg(song_name)))
        text_label = gui.customtkinter.CTkLabel(gui.central_frame,
                                                text=text,text_color='white',
                                                font=('',15))
        text_label.pack()
    elif(helpers.is_cyrillic_or_latin(song_name) == "Latin"):
        text2 = tripeSoup.get_song_text_and_chords_en((webcrawling.song_en(song_name)))
        text_label = gui.customtkinter.CTkLabel(gui.central_frame,
                                                text=text2,text_color='white',
                                                font=('',15))
        text_label.pack()
    else:
        print("song name doesn't start with a letter, fix later:D")

gui.search_song_button.configure(command=song_button_push)
gui.search_artist_button.configure(command=artist_button_push)
gui.upload_button.configure(command=upload_button_push)

gui.root.mainloop()