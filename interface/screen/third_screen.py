from typing import List
import customtkinter
from style import font
from tkinter import filedialog
import os

class Third_screen(customtkinter.CTkFrame):
    def __init__(self, master: customtkinter.CTk, font: font.FontSize):
        super().__init__(master)

        # Configure grid weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Dropdown menu for selecting audio
        self.select_audio_label = customtkinter.CTkLabel(self, text="Select Audio", font=font.md)
        self.select_audio_label.grid(row=0, column=0, pady=10, padx=10,sticky="nw")

        # TODO: Implement dropdown menu for selecting audio

        # Label for "Characters in PodifyStudio"
        self.characters_label = customtkinter.CTkLabel(self, text="Characters in PodifyStudio", font=font.xl)
        self.characters_label.grid(row=1, column=0, pady=5, padx=5, sticky="n")

        # Labels for persons
        self.person1_label = customtkinter.CTkLabel(self, text="Person 1:", font=font.md)
        self.person1_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        self.person2_label = customtkinter.CTkLabel(self, text="Person 2:", font=font.md)
        self.person2_label.grid(row=6, column=0, pady=5, padx=10, sticky="w")

        self.person3_label = customtkinter.CTkLabel(self, text="Person 3:", font=font.md)
        self.person3_label.grid(row=10, column=0, pady=5, padx=10, sticky="w")

        # Input label 
        self.person1_input = customtkinter.CTkLabel(self, text="", font=font.md)
        self.person1_input.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        self.person2_input = customtkinter.CTkLabel(self, text="", font=font.md)
        self.person2_input.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        self.person3_input = customtkinter.CTkLabel(self, text="", font=font.md)
        self.person3_input.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        # TODO: Add labels and input labels for person2 and person3

        # Button for setting intros
        self.set_intro_button = customtkinter.CTkButton(self, text="Set Intros", font=font.md)
        self.set_intro_button.grid(row=3, column=0, pady=10, padx=10, sticky="sw")

        # Button for setting outros
        self.set_outro_button = customtkinter.CTkButton(self, text="Set Outros", font=font.md)
        self.set_outro_button.grid(row=3, column=1, pady=10, padx=10, sticky="sw")

        # Button for setting background
        self.set_background_button = customtkinter.CTkButton(self, text="Set Background", font=font.md)
        self.set_background_button.grid(row=3, column=2, pady=10, padx=10, sticky="sw")

        # Next button
        self.next_button = customtkinter.CTkButton(self, text="Next", font=font.md)
        self.next_button.grid(row=4, column=0, columnspan=3, pady=20, padx=10, sticky="s")
