import customtkinter as ctk
from ..tools import read_json, write_json
# from .vertical_menu import VerticalMenu
from .horizontal_menu import HorizontalMenu
from .main_content import ContentFrame
class App(ctk.CTk):
    def __init__(self, **kwargs):
        self.CONFIG = read_json(fd= 'config.json')

        ctk.CTk.__init__(self, fg_color = "#ffffff", **kwargs)

        self.WIDTH = int(ctk.CTk.winfo_screenwidth(self) * 0.8)
        self.HEIGHT = int(ctk.CTk.winfo_screenheight(self) * 0.8)

        self.CONFIG['width'] = self.WIDTH
        self.CONFIG['height'] = self.HEIGHT
        
        write_json(fd= 'config.json', name_dict= self.CONFIG)

        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')

        # self.VERTICAL_MENU = VerticalMenu(ch_master= self)
        # self.VERTICAL_MENU.grid(row= 0, column= 0)

        self.HORIZONTAL_MENU = HorizontalMenu(ch_master= self)
        self.HORIZONTAL_MENU.grid(row= 0, column= 0)

        self.CONTENT_FRAME = ContentFrame(ch_master= self)
        self.CONTENT_FRAME.grid(row= 1, column= 0, pady= 1)
        
application = App()
