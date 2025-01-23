r'''
    Модуль розроблено з метою  надання інструкції (AppButton) для створення будь якої кнопки в графічному інтерфейсі застосунку:
    >>> class AppButton(ctk.CTkButton)

    Модулі:
    1. customtkinter - модуль GUI, що застосовується з метою розробки графічного інтерфейсу кнопки. 
    2. PIL - модуль для обробки зображень, що застосовується для завантаження зображення кнопки. Також модуль підтримує завантаження зображення кнопки з файла з директорії static/icons.
    3. os - для побудови абсолютного шляху до папки static/icons з метою завантаження графічного файлу.
    4. colorama - для надання кольру помилкам, які виводяться в термінал з функції load_image 

    Приклад застосування: 
    >>> button = AppButton(ch_master= root, name_icon='explorer.png', size= 20)
'''
import customtkinter as ctk
import PIL.Image
import os
import colorama

colorama.init(autoreset= True)
class AppButton(ctk.CTkButton):
    r'''
        Інструкція (клас) розроблена з метою створення графічного інтерфейсу кнопки
        
        Параметри класу:
        >>> ch_master: object # - вказуємо об'єкт в якому розташовуємо кнопку 
        >>> name_icon: str # - ім'я картинки, до якої потрібно побудувати абсолютний шлях
        >>> size: float # - вказуємо найменшу сторону фрейма в якому розташовується наша кнопка, а точніше її розмір, та задаємо пропорційність відносно цієї сторони у відсотках

        Приклад:
        >>> button = AppButton(ch_master= CTkFrame, name_icon='explorer.png', size= CTkFrame._current_width * 0.5)
    '''
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

    def load_image(self) -> ctk.CTkImage | None:
        '''
            Інструкція (метод), що завантажує зображення кнопки з директорії static/icons за вказанним ім'ям у властивості self.NAME_ICON
        '''
        try:
            PATH = os.path.abspath(
                os.path.join(__file__, '..', '..', '..', 'static', 'icons', self.NAME_ICON)
            )
            return ctk.CTkImage(
                light_image= PIL.Image.open(PATH),
                size= self.SIZE
            )
        except Exception as exception:
            print(f'\n{colorama.Fore.YELLOW}Error: {colorama.Fore.RED}{exception}\n')
            return None