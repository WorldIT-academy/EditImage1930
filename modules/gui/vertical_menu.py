import customtkinter as ctk
from ..tools import read_json

class VerticalMenu(ctk.CTkFrame):
    def __init__(self, ch_master: object, **kwargs):
        self.CONFIG = read_json(fd= 'config.json')
        ctk.CTkFrame.__init__(
            self, 
            master = ch_master,
            width = self.CONFIG['width'] * 0.06,
            height = self.CONFIG['height'],
            fg_color = "#181818",
            corner_radius= 0  # No corner radius for vertical menu
        )