import tkinter.filedialog as filedialog

def search_image():
    list_files = filedialog.askopenfilenames(
        title= "Search files images",
        initialdir= "/",
        filetypes= [("image files", ["*.png", "*.jpg", "*.jpeg", "*.ico"])],
        parent= None
    )
    print()
    for name_file in list_files:
        print(name_file)
    print()

