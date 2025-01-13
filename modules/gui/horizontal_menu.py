import customtkinter as ctk
from ..tools import read_json 

class HorizontalMenu(ctk.CTkFrame):
    def __init__(self, ch_master: object, **kwargs):

        self.CONFIG = read_json(fd= 'config.json')
        
        ctk.CTkFrame.__init__(
            self,
            master = ch_master,
            width = self.CONFIG['width'],
            height = self.CONFIG['height'] * 0.05,
            fg_color = "#181818",
            corner_radius= 0 
        )