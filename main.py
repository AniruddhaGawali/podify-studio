import tkinter as tk
import customtkinter

from style import font
from screen import audio_screen, podcast_screen, startup_screen, script_screen # Importing the screens
from podcast import Podcast

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Podify")
        self.font = font.FontSize("Montserrat")
        self.current_frame = None

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}+0+0")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.podcast = Podcast()


        self.startup_screen = startup_screen.StartupScreeen(self, font=self.font,podcast=self.podcast)
        self.script_screen = script_screen.ScriptScreen(self, font=self.font,next_screen=self.navigate_to_third_screen,podcast=self.podcast)
        self.audio_screen = audio_screen.AudioScreen(self,self.font,podcast=self.podcast)
        self.podcast_screen = podcast_screen.PodcastScreen(self, self.font, podcast=self.podcast)
       
        self.switch_frame(self.startup_screen)
        

    def switch_frame(self, frame: customtkinter.CTkFrame):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        
        self.current_frame = frame
        self.current_frame.pack(expand=True, fill="both")

       
    def navigate_to_script_screen(self):
        self.switch_frame(self.script_screen)

    def navigate_to_third_screen(self):
        self.switch_frame(self.audio_screen)
    
    def navigate_to_last_screen(self):
        self.switch_frame(self.podcast_screen)


if __name__ == "__main__":
    app = App()
    app.mainloop()