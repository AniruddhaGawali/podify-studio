from typing import List
import customtkinter
from podcast import Podcast
from style import font
from tkinter import filedialog
import tkinter as tk


class ScriptScreen(customtkinter.CTkFrame):
    def __init__(self,master:customtkinter.CTk,font:font.FontSize,next_screen:customtkinter.CTkFrame,podcast:Podcast):
        super().__init__(master)

        self.instruction_list = [
            "1. Add  end of the each dialog",
            "2. Add Person after each dialog"
        ]
        self.configure(fg_color="transparent")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.next_screen = next_screen
        self.podcast = podcast
        self.title_var = tk.StringVar()
        self.title_var.set("Script"+podcast.podcast_name)
       


        self.top_frame = customtkinter.CTkFrame(self)
        self.top_frame.grid(row=0, column=0, sticky="nsew", columnspan=2 ,rowspan=2)
        self.bottom_frame = customtkinter.CTkFrame(self)
        self.bottom_frame.grid(row=2, column=0, sticky="nsew")

        self.continer = customtkinter.CTkFrame(self.top_frame)
        self.continer.pack(side="left",pady=20,padx=20)
        self.continer.configure(fg_color="transparent")
        self.title= customtkinter.CTkLabel(self.continer,textvariable=self.title_var,font=font.xl3,bg_color="transparent")
        self.title.grid(row=0,column=0,pady=20,padx=20)

        self.select_script_button = customtkinter.CTkButton(self.continer,text="Open Script from Local",font=font.md,command=self.open_file)
        self.select_script_button.grid(row=1,column=0,pady=20,padx=20)
        self.select_script_button.configure(height=50,width=250)

        self.instruction_frame = customtkinter.CTkFrame(self.top_frame)
        self.instruction_frame.pack(side="right", pady=20, padx=20)

        self.instruction_title = customtkinter.CTkLabel(self.instruction_frame,text="Instructions",font=font.xl).pack(pady=30,padx=30)
        self.instructions : List[customtkinter.CTkLabel]=[]

        for i in range(0,len(self.instruction_list)):
            self.instructions.append(customtkinter.CTkLabel(self.instruction_frame,text=self.instruction_list[i]).pack(pady=5,padx=30))


        # Replace CTkEntry with CTkTextArea for multi-line input
        self.script_text_input = customtkinter.CTkTextbox(self.bottom_frame,font=font.md,width=250,padx=20, pady=20)
        self.script_text_input.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # self.next_button = customtkinter.CTkButton(self.bottom_frame, text="Next", font=font.md, command=self.bottom_frame)
        self.next_button = customtkinter.CTkButton(self.bottom_frame, text="Next", font=font.md, command=self.go_to_next_screen)
        self.next_button.grid(row=1, column=0, padx=20, pady=20,sticky="se")
        self.next_button.configure(height=50, width=250)
        

        # Configure grid row and column weights to make the text input expand
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        
      
    def open_file(self):
        path = filedialog.askopenfilename(filetypes=(('text files', '*.txt'), ('All files', '*.*') ))
        if path:
            print(path)
            self.read_txt(path=path)

    def read_txt(self,path):
        with open(path,"r") as file:
            content = file.read()
            self.script_text_input.delete("1.0", "end")
            self.script_text_input.insert("0.0",content)

    def set_title(self,title):
        self.title_var.set(title)

    def go_to_next_screen(self):
        self.podcast.set_script(self.script_text_input.get("1.0", "end"))
        self.master.audio_screen.set_options(self.podcast.get_person_from_script())
        self.master.navigate_to_third_screen()


