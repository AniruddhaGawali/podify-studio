import customtkinter
import tkinter as tk
from podcast import Podcast
from style import font

class StartupScreeen(customtkinter.CTkFrame):

    def __init__(self,master:customtkinter.CTk,font:font.FontSize,podcast:Podcast):
        super().__init__(master)
        self.pack(anchor="center",expand=True)
        self.configure(fg_color="transparent")
        self.pack_propagate(False)
        self.state=podcast
        self.title_input = tk.StringVar()
    
        self.header = customtkinter.CTkLabel(self, text="Welcome to Podify", font=font.xl5)
        self.header.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.podcastNameInput = customtkinter.CTkEntry(self, font=font.lg,placeholder_text="Enter the name of your podcast",fg_color="transparent",textvariable=self.title_input)
        self.podcastNameInput.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER,relwidth=0.3, relheight=.05)

        self.button = customtkinter.CTkButton(self, text="Get Started", font=font.md, height=50,  command=self.goto_script_screen)
        self.button.place(relx=0.5, rely=0.58 , anchor=customtkinter.CENTER, relwidth=0.25)

    def goto_script_screen(self):
        self.state.set_podcast_name(self.title_input.get())
        print(self.state.podcast_name)
        self.master.navigate_to_tab_screen()
