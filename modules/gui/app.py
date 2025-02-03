import customtkinter as ctk
from ..tools import read_json, write_json
from .frame_template import FrameTemplate
from .app_button import AppButton
from ..tools import search_image
class App(ctk.CTk):
    def __init__(self, **kwargs):
        
        self.CONFIG = read_json(fd= 'config.json')

        ctk.CTk.__init__(self, fg_color = "#ffffff", **kwargs)

        self.WIDTH = int(ctk.CTk.winfo_screenwidth(self) * self.CONFIG['app_width'])
        self.HEIGHT = int(ctk.CTk.winfo_screenheight(self) * self.CONFIG["app_height"]) 

        self.CONFIG['width'] = self.WIDTH
        self.CONFIG['height'] = self.HEIGHT
        
        write_json(fd= 'config.json', name_dict= self.CONFIG)
        #
        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.resizable(width= False, height= False)
        #
        self.HORIZONTAL_MENU = FrameTemplate(ch_master= self, ch_width= self.WIDTH, ch_height= self.HEIGHT * 0.05, ch_fg_color= "#181818")
        self.HORIZONTAL_MENU.grid(row= 0, column= 0)
        #
        self.CONTENT_FRAME = FrameTemplate(ch_master= self, ch_width= self.WIDTH, ch_height= self.HEIGHT * 0.95, ch_fg_color= "#ffffff")
        self.CONTENT_FRAME.grid(row= 1, column= 0, pady= 1)
        #
        self.VERTICAL_MENU = FrameTemplate(
            ch_master= self.CONTENT_FRAME, ch_width= self.WIDTH * 0.059, ch_height= self.HEIGHT * 0.95, ch_fg_color= "#181818")
        self.VERTICAL_MENU.grid(row= 0, column= 0)
        # self.VERTICAL_MENU.place(x =0 , y = 0)
        # 
        self.EXPLORER = FrameTemplate(
            ch_master= self.CONTENT_FRAME, ch_width= self.WIDTH * 0.179, ch_height= self.HEIGHT * 0.95, ch_fg_color= "#181818")
        self.EXPLORER.grid(row= 0, column= 1, padx= 1)
        #
        self.DASHBOARD= FrameTemplate(
            ch_master= self.CONTENT_FRAME, ch_width= self.WIDTH * 0.759, ch_height= self.HEIGHT * 0.95, ch_fg_color= "#FFFFFF")
        self.DASHBOARD.grid(row= 0, column= 2, padx= 1)
        #
        self.HEADER_DASHBOARD= FrameTemplate(
            ch_master= self.DASHBOARD, ch_width= self.DASHBOARD._current_width, ch_height= self.DASHBOARD._current_height * 0.039, ch_fg_color= "#181818" )
        self.HEADER_DASHBOARD.grid(row= 0, column= 0)
        #
        self.CONTENT_DASHBOARD= FrameTemplate(
            ch_master= self.DASHBOARD, ch_width= self.DASHBOARD._current_width, ch_height= self.DASHBOARD._current_height * 0.959, ch_fg_color= "#1f1f1f")
        self.CONTENT_DASHBOARD.grid(row= 1, column= 0, pady = 1)
        
        self.BUTTON = AppButton(
            ch_master= self.VERTICAL_MENU, 
            name_icon= 'explorer.png', 
            size= self.VERTICAL_MENU._current_width * 0.5,
            function= lambda: search_image(parent= self, button_parent= self.EXPLORER)    
        )
        self.BUTTON.place(x= 0, y= 0)
        

application = App()  
