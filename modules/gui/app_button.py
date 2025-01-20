import customtkinter as ctk
from PIL import Image
import os

class AppButton(ctk.CTkButton):
    def __init__(self, ch_master: object, name_icon: str, size: float, **kwargs):

        self.NAME_ICON = name_icon
        self.MASTER = ch_master
        self.SIZE = (int(size), int(size))

        ctk.CTkButton.__init__(
            self, 
            master= ch_master, 
            width= 0, 
            height= 0, 
            image= self.load_image(),
            text= '',
            fg_color= ch_master._fg_color,
            hover= False,
            **kwargs
        )

    def load_image(self):
        PATH = os.path.abspath(
            os.path.join(__file__, '..', '..', '..', 'static', 'icons', self.NAME_ICON)
        )
        return ctk.CTkImage(
            light_image= Image.open(PATH),
            size= self.SIZE
        )