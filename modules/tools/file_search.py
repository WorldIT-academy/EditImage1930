import tkinter.filedialog as filedialog

def search_image(parent: object):
    list_name_files = []
    list_files = filedialog.askopenfilenames(
        title= "Search files images",
        initialdir= "/",
        filetypes= [("image files", ["*.png", "*.jpg", "*.jpeg", "*.ico"])],
        parent= parent
    )
    print()
    for name_file in list_files: 
        # Example output:
        # list_files = [
        #    '/Users/worlditacademy/Downloads/photo-editing_11594650.png',
        #    '/Users/worlditacademy/Downloads/photo-editing_11594650.ico',
        #    '/Users/worlditacademy/Downloads/photo-editing_11594650-_1_.ico',
        #    '/Users/worlditacademy/Downloads/photo-editing_11594650 (1).png',
        #    '/Users/worlditacademy/Downloads/worldIT_LOGO.ico'
        # ]
        # name_file = '/Users/worlditacademy/Downloads/worldIT_LOGO.ico'
        # name_file.split('/') -> ['', 'Users', 'worlditacademy', 'Downloads', 'worldIT_LOGO.ico']
        # name_file.split('/')[-1] -> 'worldIT_LOGO.ico'
        print(name_file.split('/')[-1]) # -> worldIT_LOGO.ico
        list_name_files.append(name_file.split("/")[-1])
    print()

