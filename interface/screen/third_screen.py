import tkinter as tk
from typing import List
import customtkinter
from customtkinter import CTkOptionMenu
from style import font
from tkinter import filedialog  
import os

class Third_screen(customtkinter.CTkFrame):
    def __init__(self, master: customtkinter.CTk, font: font.FontSize):
        super().__init__(master)

        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row = 0, column = 0, padx = 1, pady = 125, columnspan = 10)
        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row = 1, column = 0, padx = 200, pady = 1, rowspan = 10)

        self.select_audio_label = customtkinter.CTkLabel(self, text="Select Audio", font=font.md)
        self.select_audio_label.grid(row=1, column=1, pady=10, padx=10,columnspan=10,sticky="nw")

        # TODO: Implement dropdown menu for selecting audio

        # Label for "Characters in PodifyStudio"
        self.characters_label = customtkinter.CTkLabel(self, text="Characters in PodifyStudio", font=font.xl3)
        self.characters_label.grid(row=2, column=3, pady=5, padx=5,sticky="n")
        

        # Labels for persons
        self.person1_label = customtkinter.CTkLabel(self, text="Person 1:", font=font.md)
        self.person1_label.grid(row=3, column=1, pady=15, padx=30, sticky="w")

        self.person2_label = customtkinter.CTkLabel(self, text="Person 2:", font=font.md)
        self.person2_label.grid(row=4, column=1, pady=15, padx=30, sticky="w")

        self.person3_label = customtkinter.CTkLabel(self, text="Person 3:", font=font.md)
        self.person3_label.grid(row=5, column=1, pady=15, padx=30, sticky="w")

        self.person4_label = customtkinter.CTkLabel(self, text="Person 4:", font=font.md)
        self.person4_label.grid(row=6, column=1, pady=15, padx=30, sticky="w")

        # Input label 

        options = ["Option 1", "Option 2", "Option 3", "Option 4"]
        self.option_var = tk.StringVar(self)
        self.option_var.set(options[0])  # Set default value

        def optionmenu_callback(choice):
            print("Selected option:", choice)

        self.combobox = customtkinter.CTkOptionMenu(self, variable=self.option_var, command=optionmenu_callback, values=options)
        self.combobox.grid(row=3, column=2, pady=15, padx=30, columnspan=1)

        self.combobox = customtkinter.CTkOptionMenu(self, variable=self.option_var, command=optionmenu_callback, values=options)
        self.combobox.grid(row=4, column=2, pady=15, padx=30, columnspan=1)

        self.combobox = customtkinter.CTkOptionMenu(self, variable=self.option_var, command=optionmenu_callback, values=options)
        self.combobox.grid(row=5, column=2, pady=15, padx=30, columnspan=1)

        self.combobox = customtkinter.CTkOptionMenu(self, variable=self.option_var, command=optionmenu_callback, values=options)
        self.combobox.grid(row=6, column=2, pady=15, padx=30, columnspan=1)


        self.person1_input = customtkinter.CTkLabel(self, text="", font=font.md)
        self.person1_input.grid(row=3, column=2, pady=15, padx=30, sticky="w")

        self.person2_input = customtkinter.CTkLabel(self, text="", font=font.md)
        self.person2_input.grid(row=4, column=2, pady=15, padx=30, sticky="w")

        self.person3_input = customtkinter.CTkLabel(self, text="", font=font.md)
        self.person3_input.grid(row=5, column=2, pady=15, padx=30, sticky="w")

        self.person4_input = customtkinter.CTkLabel(self, text="", font=font.md)
        self.person4_input.grid(row=6, column=2, pady=15, padx=30, sticky="w")

        # TODO: Add labels and input labels for person2 and person3

        # Button for setting intros
        self.set_intro_button = customtkinter.CTkButton(self, text="Set Intros", font=font.md)
        self.set_intro_button.grid(row=7, column=2, pady=10, padx=10)

        # Button for setting outros
        self.set_outro_button = customtkinter.CTkButton(self, text="Set Outros", font=font.md)
        self.set_outro_button.grid(row=7, column=3, pady=10, padx=10)

        # Button for setting background
        self.set_background_button = customtkinter.CTkButton(self, text="Set Background", font=font.md)
        self.set_background_button.grid(row=7, column=4, pady=10, padx=10)

        # Next button
        self.next_button = customtkinter.CTkButton(self, text="Next", font=font.md , command=self.navigate_to_last_screen)
        self.next_button.grid(row=8, column=2, columnspan=3, pady=20, padx=10, sticky="s")

    def navigate_to_last_screen(self):
        self.master.navigate_to_last_screen()