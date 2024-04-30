import customtkinter
from style import font

class StartupScreeen(customtkinter.CTkFrame):

    def __init__(self,master:customtkinter.CTk,font:font.FontSize):
        super().__init__(master)
        self.pack(anchor="center",expand=True)
        self.configure(fg_color="transparent")
        self.pack_propagate(False)
    
        self.header = customtkinter.CTkLabel(self, text="Welcome to Podify", font=font.xl5)
        self.header.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.button = customtkinter.CTkButton(self, text="Get Started", font=font.md, height=50,  command=self.goto_script_screen)
        self.button.place(relx=0.5, rely=0.5 , anchor=customtkinter.CENTER, relwidth=0.25)

    def goto_script_screen(self):
        self.master.switch_frame(self.master.script_screen)




