import customtkinter as ctk
from ..tools import read_json, write_json
from .frame_template import FrameTemplate

class App(ctk.CTk):
    def __init__(self, **kwargs):
        
        self.CONFIG = read_json(fd= 'config.json')

        ctk.CTk.__init__(self, fg_color = "#ffffff", **kwargs)

        self.WIDTH = int(ctk.CTk.winfo_screenwidth(self) * self.CONFIG['app_width'])
        self.HEIGHT = int(ctk.CTk.winfo_screenheight(self) * self.CONFIG["app_height"]) 

        self.CONFIG['width'] = self.WIDTH
        self.CONFIG['height'] = self.HEIGHT
        
        write_json(fd= 'config.json', name_dict= self.CONFIG)

        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')

        self.HORIZONTAL_MENU = FrameTemplate(ch_master= self, ch_width= self.WIDTH, ch_height= self.HEIGHT * 0.05, ch_fg_color= "#181818")
        self.HORIZONTAL_MENU.grid(row= 0, column= 0)

        self.CONTENT_FRAME = FrameTemplate(ch_master= self, ch_width= self.WIDTH, ch_height= self.HEIGHT * 0.95, ch_fg_color= "#1f1f1f")
        self.CONTENT_FRAME.grid(row= 1, column= 0, pady= 1)
        
application = App()  
