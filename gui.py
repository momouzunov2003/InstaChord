from tkinter import filedialog
import tkinter
import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("InstaChord")
root.iconbitmap("Images\instachord-high-resolution-logo-transparent.ico")
screen_width = str(root.winfo_screenwidth())
screen_height = str(root.winfo_screenheight())
geometry_string = screen_width + 'x' + screen_height
root.geometry(geometry_string)
root.resizable(True, True)
root.after(0, lambda:root.state('zoomed'))

top_frame = customtkinter.CTkFrame(root,fg_color="#383b39",
                                   height=40,
                                   corner_radius=0)
top_frame.pack(fill="x",side="top")

search_textbox = customtkinter.CTkEntry(top_frame,
                                        height=20,
                                        fg_color="white",
                                        border_color="white",
                                        text_color="black",
                                        placeholder_text="Search for any song or artist")
search_textbox.pack(expand=False,
                    pady=5,
                    padx=10,
                    ipadx=50,
                    side="left")

search_song_button = customtkinter.CTkButton(top_frame,
                                        height=23,
                                        width=5,
                                        text="Search for a song")
search_song_button.pack(side="left", pady=5)

search_artist_button = customtkinter.CTkButton(top_frame,
                                        height=23,
                                        width=5,
                                        text="Search for an artist")
search_artist_button.pack(side="left", pady=5, padx=5)

upload_button = customtkinter.CTkButton(top_frame,
                                        height=23,
                                        width=5,
                                        text="Upload a song from file")
upload_button.pack(side="right",
                   padx=10,
                   pady=5,
                   ipadx=10)

bottom_frame = customtkinter.CTkFrame(root,fg_color="#383b39", height=30, corner_radius=0)
bottom_frame.pack(side="bottom", fill="x")

credits = customtkinter.CTkLabel(bottom_frame,text="© 2024 InstaChord. Всички права запазени.", text_color="#595e5b")
credits.pack()

central_frame = customtkinter.CTkFrame(root, fg_color="#383b39")
central_frame.pack(fill="both",
                   expand=True,
                   pady=3,
                   padx=3)