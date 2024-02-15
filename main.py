import gui
import spotifyAPI
import webcrawling
import helpers

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
    #TODO: Make find song function and insert as choice_button function!!!

def song_button_push():
    for widget in gui.central_frame.winfo_children():
        widget.destroy()

    song_name = gui.search_textbox.get()

    if(helpers.is_cyrillic_or_latin(song_name) == "Cyrillic"):
        webcrawling.song_bg(song_name)
    elif(helpers.is_cyrillic_or_latin(song_name) == "Latin"):
        webcrawling.song_en(song_name)
    else:
        print("song name doesn't start with a letter, fix later:D")


    
    
    
gui.search_song_button.configure(command=song_button_push)
gui.search_artist_button.configure(command=artist_button_push)

gui.root.mainloop()