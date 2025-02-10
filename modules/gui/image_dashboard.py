import customtkinter as ctk
from ..tools import read_json
import PIL.Image

class ImageLabel(ctk.CTkLabel):
    def __init__(self, ch_master: ctk.CTkFrame, path_file: str,  **kwargs):
        self.PATH_FILE = path_file
        self.NAME_IMAGE = path_file.split('/')[-1]
        
        self.WIDTH = int(ch_master._current_width * 0.9)
        self.HEIGHT = int(ch_master._current_height * 0.9)
        
        ctk.CTkLabel.__init__(
            self,
            master= ch_master,
            image= self.load_image(),
            text= '',
            **kwargs
        )
    
    def load_image(self):
        # dict_path_file = read_json(fd= "path_files.json")
        image = PIL.Image.open(self.PATH_FILE) # image.width, image.height
        
        try:
            return ctk.CTkImage(
                light_image= image,
                size= self.image_size(image = image)
                # if image.width >= self.WIDTH and image.height >= self.HEIGHT: 
                #     return (self.WIDTH, self.HEIGHT)
                # else:
                #     return (image.width, image.height)
            )
        except Exception as error:
            print(f'Error while loading image: {error}')
            return None
    def image_size(self, image: PIL.Image) -> tuple[int, int]:
        # Якщо зображення у формі квадрата
        if image.width == image.height:
            if image.width >= self.WIDTH and image.height >= self.HEIGHT:
                return (self.HEIGHT, self.HEIGHT)
            elif image.width < self.WIDTH and image.height < self.HEIGHT:
                return (image.width, image.height)
            else:
                return (self.HEIGHT, self.HEIGHT)
        # Якщо зображення у формі прямокутника
        else:
            if image.width >= self.WIDTH and image.height >= self.HEIGHT:
                return (self.WIDTH, self.HEIGHT)
            elif image.width < self.WIDTH and image.height < self.HEIGHT:
                return (image.width, image.height)
            else:
                return (self.WIDTH, self.HEIGHT)
            

        
        
    
