import tkinter as tk
from typing import List
import customtkinter
from customtkinter import CTkOptionMenu
from podcast import Podcast
from style import font
from tkinter import filedialog  
from text_to_audio import TextToAudio
from pydub import AudioSegment

class AudioScreen(customtkinter.CTkFrame):
    def __init__(self, master: customtkinter.CTk, font: font.FontSize,podcast:Podcast):
        super().__init__(master)

        self.podcast = podcast
        self.font= font 

        

        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row = 0, column = 0, padx = 1, pady = 125, columnspan = 10)
        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row = 1, column = 0, padx = 200, pady = 1, rowspan = 10)

        self.select_audio_label = customtkinter.CTkLabel(self, text="Select Audio", font=font.md)
        self.select_audio_label.grid(row=1, column=1, pady=10, padx=10,columnspan=10,sticky="nw")

        self.current_row = 3
        self.persons=[]
        self.intro = None
        self.outro = None
        self.background = None

       

        # Label for "Characters in PodifyStudio"
        self.characters_label = customtkinter.CTkLabel(self, text="Characters in PodifyStudio", font=font.xl3)
        self.characters_label.grid(row=2, column=3, pady=5, padx=5,sticky="n")

        self.options = [item for sublist in [TextToAudio.allVoiceInGTTS()] for item in sublist]
        

        # Button for setting intros
        self.set_intro_button = customtkinter.CTkButton(self, text="Set Intro", font=font.md,command=self.set_intro)
        self.set_intro_button.grid(row=self.current_row+1, column=2, pady=10, padx=10)

        # Button for setting outros
        self.set_outro_button = customtkinter.CTkButton(self, text="Set Outro" ,font=font.md,command=self.set_outro)
        self.set_outro_button.grid(row=self.current_row+1, column=3, pady=10, padx=10)

        # Button for setting background
        self.set_background_button = customtkinter.CTkButton(self, text="Set Background Music", font=font.md ,command=self.set_background)
        self.set_background_button.grid(row=self.current_row+1, column=4, pady=10, padx=10)

        # Next button
        self.next_button = customtkinter.CTkButton(self, text="Generate", font=font.md , command=self.navigate_to_last_screen)
        self.next_button.grid(row=self.current_row+2, column=2, columnspan=3, pady=20, padx=10, sticky="s")

    def optionmenu_callback(self,choice):
            newDict ={}

            for i in self.persons:
                found_object = next((obj for obj in self.options if obj.get('name') == i[1].get()), None)
                newDict[i[0].cget("text")]= found_object.get('id')

            print(newDict)
            self.podcast.set_person_audio(newDict)
               

    def navigate_to_last_screen(self):
        self.podcast.generate_podcast()
        # self.master.navigate_to_last_screen()

    def add_persons(self, persons: List[str]):
       values = [item['name'] for item in self.options]
        
       for i in persons:
            
            form = [
                customtkinter.CTkLabel(self, text=i, font=self.font.md),
                customtkinter.CTkOptionMenu(self, variable=tk.StringVar(self).set(values[0]), command=self.optionmenu_callback, values=values)
            ]
            form[0].grid(row=self.current_row, column=1, pady=15, padx=30, sticky="w"),
            form[1].grid(row=self.current_row, column=2, pady=15, padx=30, columnspan=1),

            self.persons.append(form)
            self.current_row += 1
            self.set_intro_button.grid(row=self.current_row+1, column=2, pady=10, padx=10)
            self.set_outro_button.grid(row=self.current_row+1, column=3, pady=10, padx=10)
            self.set_background_button.grid(row=self.current_row+1, column=4, pady=10, padx=10)
            self.next_button.grid(row=self.current_row+2, column=2, columnspan=3, pady=20, padx=10, sticky="s")
            

    def set_options(self, persons: List[str]):
        self.add_persons(persons=persons)

    def set_intro(self):
        path = filedialog.askopenfilename(filetypes=(('audio file', '*.wav'),('audio file', '*.mp3'), ('All files', '*.*') ))
        if path:
            print(path)
            self.intro = path
            self.set_intro_button.configure(text="Change Intro : "+path.split("/")[-1])
            audio = AudioSegment.from_file(path)
            self.podcast.set_intro(audio)


    def set_outro(self):
        path = filedialog.askopenfilename(filetypes=(('audio file', '*.wav'),('audio file', '*.mp3'), ('All files', '*.*') ))
        if path:
            print(path)
            self.outro = path
            self.set_outro_button.configure(text="Change Outro : "+path.split("/")[-1])
            audio = AudioSegment.from_file(path)
            self.podcast.set_outro(audio)

    def set_background(self):
        path = filedialog.askopenfilename(filetypes=(('audio file', '*.wav'),('audio file', '*.mp3'), ('All files', '*.*') ))
        if path:
            print(path)
            self.background = path
            self.set_background_button.configure(text="Change Background Music : "+path.split("/")[-1])
            audio = AudioSegment.from_file(path)
            self.podcast.set_background_music(audio)
