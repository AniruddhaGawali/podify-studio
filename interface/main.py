import tkinter as tk
import customtkinter
from style import font
from screen import startup_screen, script_screen ,third_screen , last_screen # Importing the screens

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

        self.startup_screen = startup_screen.StartupScreeen(self, self.font)
        self.script_screen = script_screen.ScriptScreen(self, self.font)
        self.third_screen = third_screen.Third_screen(self,self.font)
        self.last_screen = last_screen.Last_screen(self, self.font)

        self.switch_frame(self.startup_screen)

    def switch_frame(self, frame: customtkinter.CTkFrame):
        if self.current_frame is not None:
            self.current_frame.pack_forget()

        self.current_frame = frame
        self.current_frame.pack(expand=True, fill="both")

    def navigate_to_third_screen(self):
        self.switch_frame(self.third_screen)
    
    def navigate_to_last_screen(self):
        self.switch_frame(self.last_screen)


if __name__ == "__main__":
    app = App()
    app.mainloop()

