import customtkinter as ctk

class FrameTemplate(ctk.CTkFrame):
    def __init__(self, ch_master: object, ch_width: int, ch_height: int, ch_fg_color: str, **kwargs):
        ctk.CTkFrame.__init__(
            self,
            master= ch_master,
            width= ch_width,
            height= ch_height,
            fg_color= ch_fg_color,
            corner_radius= 0,
            **kwargs
        )
        