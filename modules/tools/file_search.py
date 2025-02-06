import tkinter.filedialog as filedialog
from ..gui.app_button import AppButton
import customtkinter as ctk
from .write_json import write_json
from ..gui.image_dashboard import ImageLabel

list_image = []
list_button = []

def show_image():
    for button in list_button:
        print(button.TEXT)
        for image in list_image:
            print(image.NAME_IMAGE)
            if button.TEXT == image.NAME_IMAGE:
                image.pack()


                
                

def search_image(parent: ctk.CTk, button_parent: ctk.CTkScrollableFrame | ctk.CTkFrame, content_dashboard: ctk.CTkFrame):
    r'''
    Function for search image files in directory and create buttons with their names.
     - :mod:`parent`- object, parent application
     - :mod:`button_parent`- object, frame where buttons will be created
    '''
    
    # list_name_files = []
    dict_path_files = dict()
    
    list_files = filedialog.askopenfilenames(
        title= "Search files images",
        initialdir= "/",
        filetypes= [("image files", ["*.png", "*.jpg", "*.jpeg", "*.ico"])],
        parent= parent
    )
    print()
    for path_file in list_files: 
        # Example output:
        # list_files = [
        #    '/Users/worlditacademy/Downloads/photo-editing_11594650.png',
        #    '/Users/worlditacademy/Downloads/photo-editing_11594650.ico',
        #    '/Users/worlditacademy/Downloads/photo-editing_11594650-_1_.ico',
        #    '/Users/worlditacademy/Downloads/photo-editing_11594650 (1).png',
        #    '/Users/worlditacademy/Downloads/worldIT_LOGO.ico'
        # ]
        # path_file = '/Users/worlditacademy/Downloads/worldIT_LOGO.ico'
        # path_file.split('/') -> ['', 'Users', 'worlditacademy', 'Downloads', 'worldIT_LOGO.ico']
        # path_file.split('/')[-1] -> 'worldIT_LOGO.ico'
        name_file = path_file.split('/')[-1] # -> 'worldIT_LOGO.ico'
        type_file = name_file.split('.')[-1] # -> ['worldIT_LOGO', 'ico']
        # print(name_file) 
        # list_name_files.append(path_file)
        dict_path_files[name_file] = path_file
        #
        list_image.append(ImageLabel(ch_master= content_dashboard, path_file= path_file))
        #
        button = AppButton(
            ch_master = button_parent, 
            text_button = name_file,
            # if len(name_file) > 12:
            #     return f'{name_file[0:12]}...    .{type_file}'
            # else:
            #     return name_file
            function= show_image
        )
        button.pack(pady = 20, padx = 20, anchor = 'w')
        list_button.append(button)

    # write_json(fd= "path_files.json", name_dict= dict_path_files)
    print(f'Found {len(list_image)} image files.')

    print()

