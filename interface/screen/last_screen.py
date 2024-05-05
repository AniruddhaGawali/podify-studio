from typing import List
import customtkinter
from style import font
from tkinter import filedialog
import os

class Last_screen(customtkinter.CTkFrame):
    def __init__(self, master: customtkinter.CTk, font: font.FontSize):
        super().__init__(master)