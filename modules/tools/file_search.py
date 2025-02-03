import tkinter.filedialog as filedialog
from ..gui.app_button import AppButton
import customtkinter as ctk

def search_image(parent: object, button_parent: ctk.CTkFrame):
    r'''
    Function for search image files in directory and create buttons with their names.
     - :mod:`parent`- object, parent application
     - :mod:`button_parent`- object, frame where buttons will be created
    '''
    
    list_name_files = []
    
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
        print(name_file) 
        list_name_files.append(name_file)
        
        button = AppButton(
            ch_master = button_parent, 
            text_button = f'{name_file[0:12]}...    .{type_file}' if len(name_file) > 12 else name_file
            # if len(name_file) > 12:
            #     return f'{name_file[0:12]}...    .{type_file}'
            # else:
            #     return name_file
        )
        
        button.pack(pady = 20, padx = 20, anchor = 'w')
        button_parent.pack_propagate(False)
    print()

