import customtkinter as ctk
from ..tools import read_json

class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        
        self.WIDTH = int(self.winfo_screenwidth() * 0.8)
        self.HEIGHT = int(self.winfo_screenheight() * 0.8)
        
        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')


application = App()