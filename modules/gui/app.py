import customtkinter as ctk
from ..tools import read_json
from ..tools import write_json

from .vertical_menu import VerticalMenu

class App(ctk.CTk):
    def __init__(self, **kwargs):
        self.CONFIG = read_json(fd= 'config.json')

        ctk.CTk.__init__(self, fg_color = "#1f1f1f", **kwargs)

        self.WIDTH = int(ctk.CTk.winfo_screenwidth(self) * 0.8)
        self.HEIGHT = int(ctk.CTk.winfo_screenheight(self) * 0.8)

        self.CONFIG['width'] = self.WIDTH
        self.CONFIG['height'] = self.HEIGHT
        
        write_json(fd= 'config.json', name_dict= self.CONFIG)

        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')

        self.VERTICAL_MENU = VerticalMenu(ch_master= self)
        self.VERTICAL_MENU.grid(row= 0, column= 0)
        # self.VERTICAL_MENU_INFO = ctk.CTkFrame(master = self, width= self.WIDTH * 0.15, height= self.HEIGHT, fg_color= "#181818")
        # self.VERTICAL_MENU_INFO.grid(row= 0, column= 1, padx= 2)


application = App()