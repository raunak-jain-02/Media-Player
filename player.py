import customtkinter as ctk
from tkinter import filedialog
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Initialize main window
ctk.set_appearance_mode("dark")  # Dark mode like Spotify
root = ctk.CTk()
root.title("Python Spotify")
root.geometry("400x500")

# Global variables
playlist = []
current_index = 0

# Function to load multiple songs
def load_songs():
    global playlist
    files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav")])
    playlist = list(files)
    if playlist:
        play_song(0)

# Function to play a song from the playlist
def play_song(index):
    global current_index
    if 0 <= index < len(playlist):
        current_index = index
        pygame.mixer.music.load(playlist[current_index])
        pygame.mixer.music.play()
        song_label.configure(text=os.path.basename(playlist[current_index]))

# Play/Pause toggle
def toggle_play():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

# Stop playback
def stop():
    pygame.mixer.music.stop()

# Next song
def next_song():
    play_song((current_index + 1) % len(playlist))

# Previous song
def prev_song():
    play_song((current_index - 1) % len(playlist))

# Volume control
def set_volume(val):
    pygame.mixer.music.set_volume(float(val) / 100)

# UI Elements
song_label = ctk.CTkLabel(root, text="No song playing", font=("Arial", 16))
song_label.pack(pady=10)

btn_load = ctk.CTkButton(root, text="Load Songs", command=load_songs)
btn_load.pack(pady=5)

btn_play = ctk.CTkButton(root, text="Play/Pause", command=toggle_play)
btn_play.pack(pady=5)

btn_stop = ctk.CTkButton(root, text="Stop", command=stop)
btn_stop.pack(pady=5)

btn_prev = ctk.CTkButton(root, text="Previous", command=prev_song)
btn_prev.pack(pady=5)

btn_next = ctk.CTkButton(root, text="Next", command=next_song)
btn_next.pack(pady=5)

volume_slider = ctk.CTkSlider(root, from_=0, to=100, command=set_volume)
volume_slider.set(50)  # Default volume at 50%
volume_slider.pack(pady=10)

root.mainloop()
