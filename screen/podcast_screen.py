from typing import List
import customtkinter
from style import font
from tkinter import filedialog
import os

class PodcastScreen(customtkinter.CTkFrame):
    def __init__(self, master: customtkinter.CTk, font: font.FontSize):
        super().__init__(master)


        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row = 0, column = 0, padx = 680, pady = 10, columnspan = 10)
        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row = 10, column = 0, padx = 20, pady = 200, rowspan = 10)

        # Cross symbol to quit the program
        self.quit_button = customtkinter.CTkButton(self, text="❌", font=font.md, command=self.quit_program)
        self.quit_button.grid(row=0, column=10, padx=10, pady=10)

        # Label indicating "All Done"
        self.all_done_label = customtkinter.CTkLabel(self, text="All Done", font=font.xl)
        self.all_done_label.grid(row=9, column=4, columnspan=3, pady=20)

        # Label indicating "Your Customized Podcast"
        self.customized_label = customtkinter.CTkLabel(self, text="Your Customized Podcast", font=font.xl2)
        self.customized_label.grid(row=10, column=4, columnspan=3, pady=20)

        # Button to edit the podcast
        self.edit_button = customtkinter.CTkButton(self, text="Edit", font=font.md, command=self.edit_podcast)
        self.edit_button.grid(row=13, column=4, padx=10, pady=10)

        # Button to save the podcast
        self.save_button = customtkinter.CTkButton(self, text="Save", font=font.md, command=self.save_podcast)
        self.save_button.grid(row=13, column=5, padx=10, pady=10)

    def quit_program(self):
        # Add code to quit the program gracefully
        self.master.quit()

    def edit_podcast(self):
        # Add code to handle editing the podcast
        pass

    def save_podcast(self):
        # Add code to handle saving the podcast
        pass