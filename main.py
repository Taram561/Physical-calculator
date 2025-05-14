import customtkinter as ctk
from PIL import Image
import os
import tkinter as tk

'''
Цвет фона - #2B2B2B
'''

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ''' 
        Настройка функций окна
        
        title: Установка названия окна
        window_width: Запрос ширины экрана
        window_height: Запрос высоты экрана
        geometry: Установка разрешения окна приложения
        attributes: Установка для окна полноэкранного режима
        set_appearance_mode: Установка тёмной темы окна                                   
        current_path: Ищет путь до нужного файла
        background_image: Загружает нужное изображение на фон интерфейса
        close_image_button: Загружает изображение для кнопки закрытия приложения
        close_button: Кнопка закрытия приложения
        '''
        
        self.title("Калькулятор")
        #self.window_width = self.winfo_screenwidth()
        #self.window_height = self.winfo_screenheight()
        #self.geometry(f"{self.window_width}x{self.window_height}")
        self.attributes("-fullscreen", True) 
        ctk.set_appearance_mode("dark")

        # Загрузить и создать фоновое изображение
        current_path = os.path.dirname(os.path.realpath(__file__))
        background_image = ctk.CTkImage(Image.open(current_path + "\\images\\fon_3.jpg"),
                                size = (self.winfo_screenwidth(), self.winfo_screenheight()))
        background_image_label = ctk.CTkLabel(self, image = background_image, text = '')
        background_image_label.grid(column = 0, row = 0)

        
        # Создание кнопки закрытия приложения
        close_image_button = ctk.CTkImage(dark_image = Image.open(current_path + '\\images\\115.png'), size = (30, 30))
        
        close_button = ctk.CTkButton(self,
                                     image = close_image_button,
                                     text = '',
                                     command = lambda: app.destroy(),
                                     width = 5, height = 5,
                                     fg_color = "#384454")
        close_button.grid(column = 0, row = 0,
                          sticky = 'nw')
        
        
        # Создание стартового фрейма
        self.start_frame = ctk.CTkFrame(self, corner_radius = 10)
        self.start_frame.grid(column = 0, row = 0, 
                              sticky = "nse")

        self.start_label = ctk.CTkLabel(self.start_frame,
                                        text = "Добро пожаловать "
                                               "\nВ калькулятор "
                                               "\nПо главе физики "
                                               "\n\"Механика\"",
                                        font = ctk.CTkFont(size = 80, weight = "bold"))
        self.start_label.grid(column = 0, row = 0,
                              padx = 30, pady = (250, 15),
                              sticky = 'nsew')

        # Кнопка перехода на главный фрейм
        self.start_button = ctk.CTkButton(self.start_frame,
                                          text = "Начать работу",
                                          command = self.start_event,
                                          width = 480, height = 100,
                                          corner_radius = 100,
                                          font = ctk.CTkFont(size = 60, weight = "bold"))
        
        self.start_button.grid(column = 0, row = 1,
                               padx = 30, pady = (15, 15))
        
        # Кнопка перехода на страницу инструкции
        self.instructions_button = ctk.CTkButton(self.start_frame,
                                                 text = "Инструкция",
                                                 command = self.instructions_event,
                                                 width = 510, height = 100,
                                                 corner_radius = 100,
                                                 font = ctk.CTkFont(size = 60, weight = "bold"))
        self.instructions_button.grid(column = 0, row = 2,
                               padx = 30, pady = (15, 15))
        
        
        # Создание фрейма инструкции
        self.instructions_frame = ctk.CTkScrollableFrame(self, 
                                                         width = 782,
                                                         corner_radius = 10)
        self.instructions_frame.grid_remove()
        
        # Кнопка возврата на стартовый фрейм
        back_to_start_button = ctk.CTkButton(self.instructions_frame,
                                             text = "Вернуться на"
                                                    "\nначальную страницу",
                                             command = self.instructions_back_event,
                                             width = 510, height = 100,
                                             corner_radius = 100,
                                             font = ctk.CTkFont(size = 60, weight = "bold"))
        back_to_start_button.grid(column = 0, row = 0,
                                  padx = 30, pady = (15, 15))
        
        instructions_image = ctk.CTkImage(Image.open(current_path + "/images/Inst1.1.png"),
                                          size = (782, 285))
        instructions_image_label = ctk.CTkLabel(self.instructions_frame, image = instructions_image, text = '')
        instructions_image_label.grid(column = 0, row = 1)
        
        instructions_label = ctk.CTkLabel(self.instructions_frame,
                                          text = "Инструкция по \nиспользованию калькулятора:",
                                          font = ctk.CTkFont(size = 50, weight = "bold"))
        instructions_label.grid(column = 0, row = 2)
        
        instructions_1_label = ctk.CTkLabel(self.instructions_frame,
                                          text = "\n1. Если величина дана не целым числом, "
                                                 "\nвместо запятой вводить данные через точку. "
                                                 "\nПример: Дано: 9,8; Вводить: 9.8"
                                                 "\n"
                                                 "\n2. Если дано несколько переменных одной "
                                                 "\nвеличины, их следует вводить через пробел"
                                                 "\nот конечной к начальной",
                                          font = ctk.CTkFont(size = 30, weight = "bold"))
        instructions_1_label.grid(column = 0, row = 3, sticky = "we")
        
        # Создание главного фрейма
        self.main_frame = main_frame(master = self)
        self.main_frame.grid_remove()
        


     
        
       
    def start_event(self):        
        
        # Сокрытие стартового фрейма
        self.start_frame.grid_remove()
        self.main_frame.grid(column=0, row=0,
                             sticky="nse")
        
    def instructions_event(self):
        self.start_frame.grid_forget()
        self.instructions_frame.grid(column=0, row=0,
                             sticky="nse")
        
    def instructions_back_event(self):
        self.start_frame.grid(column=0, row=0,
                             sticky="nse")
        self.instructions_frame.grid_forget()
        
               
class main_frame(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)


        self.instructions_label_main = ctk.CTkLabel(self,
                                                    text = "Введите доступные данные и"
                                                           "\nотметьте которые требуется найти"
                                                           "\n(если требуется выберите единицы"
                                                           "\nизмерения, входных и выходных данных)",
                                                    width = 800, height = 100,
                                                    corner_radius = 40,
                                                    font = ctk.CTkFont(size = 37, weight = "bold"))
        self.instructions_label_main.grid(column = 0, row = 1,
                                          padx = 20, pady = 10)

        #Создание фрейма ввода данных
        self.main_Scroll_Frame = ctk.CTkScrollableFrame(self,
                                                        width = 830, height = 380,
                                                        corner_radius = 20)
        self.main_Scroll_Frame.grid(column = 0, row = 3)
                                                                   
        self.radio_system = tk.IntVar(value = 0)  
        self.radiobutton_whibth = ctk.CTkRadioButton(self.main_Scroll_Frame,
                                                     text = "Тело движется по оси x "
                                                            "\n(По горизонтали)",
                                                     command = self.show_openMenu_X,
                                                     variable = self.radio_system, value = 1,
                                                     width = 100, height = 22,
                                                     radiobutton_width = 25, radiobutton_height = 25,
                                                     font = ctk.CTkFont(size = 20, weight = "bold"))
        self.radiobutton_whibth.grid(column = 0, row = 0, 
                                    padx = (70, 5), pady = 5,
                                    sticky = "w")                                                                                                                            
        
        self.radiobutton_height = ctk.CTkRadioButton(self.main_Scroll_Frame,
                                                     text = "Тело движется по оси y "
                                                            "\n(По вертикали)",
                                                     variable = self.radio_system, value = 2,
                                                     command = self.show_openMenu_Y,
                                                     width = 100, height = 22,
                                                     radiobutton_width = 25, radiobutton_height = 25,
                                                     font = ctk.CTkFont(size = 20, weight = "bold"))
        self.radiobutton_height.grid(column = 0, row = 0,
                                     padx = (5, 130), pady = 5,
                                     sticky = "e")
                                                        
        self.horizontal_system_combobox_var = ctk.StringVar(value ="вперёд")
        self.horizontal_system_combobox = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                                            values = ["вперёд", "назад"],
                                                            variable = self.horizontal_system_combobox_var,
                                                            width = 125, height = 35,
                                                            font = ctk.CTkFont(size = 20, weight = "bold"), )
        self.horizontal_system_combobox.grid_remove()
                                                                                
                                                        
        self.vertical_system_combobox_var = ctk.StringVar(value ="вверх")
        self.vertical_system_combobox = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                                          values = ["вверх", "вниз"],
                                                          variable = self.vertical_system_combobox_var,
                                                          width = 125, height = 35,
                                                          font = ctk.CTkFont(size = 20, weight="bold"))
        self.vertical_system_combobox.grid_remove()

                                                        
                                                        
        self.radio_move = tk.IntVar(value = 0)              
        self.check_var_equally_speed = ctk.StringVar(value = "off")
        self.checkbox_equally_speed = ctk.CTkRadioButton(self.main_Scroll_Frame,
                                                         text = "Тело движется равномерно",
                                                         variable = self.radio_move,
                                                         command = self.boost_move_event,
                                                         value = 1,
                                                         width = 100, height = 24,
                                                         radiobutton_width = 25, radiobutton_height = 25,
                                                         font = ctk.CTkFont(size = 20, weight = "bold"))
        self.checkbox_equally_speed.grid(column = 0, row = 1,
                                        padx = (70, 0), pady = 5,
                                        sticky = "w")
                        
        
        self.check_var_equally_boost = ctk.StringVar(value = "off")
        self.checkbox_equally_boost = ctk.CTkRadioButton(self.main_Scroll_Frame,
                                                         text = "Тело движется с ускорением",
                                                         variable = self.radio_move,
                                                         width = 100, height = 20,
                                                         command = self.pram_move_event,
                                                         value = 2,
                                                         radiobutton_width = 25, radiobutton_height = 25,
                                                         font = ctk.CTkFont(size = 20, weight = "bold"))
        self.checkbox_equally_boost.grid(column = 0, row = 1,
                                        padx = (5, 50), pady = 5,
                                        sticky = "e")
        
        
        
        
        
                        
        # Ускорение    
        self.check_var_boost = ctk.StringVar(value = "off")                        
        self.boost_label = ctk.CTkCheckBox(self.main_Scroll_Frame,
                                           text = "Ускорение (a)",
                                           command = lambda: self.boost_result.grid(column = 0, row = 4,
                                                                                    sticky = "w") if self.check_var_boost.get() == "on"
                                                                                              else self.boost_result.grid_remove(),
                                           variable = self.check_var_boost,
                                           onvalue = "on", offvalue = "off",
                                           width = 100, height = 20,
                                           checkbox_width = 24, checkbox_height = 24,
                                           font = ctk.CTkFont(size = 20, weight = "bold"))
        self.boost_label.grid(column = 0,row = 4,
                              padx = (106, 40), pady = 5, 
                              sticky = 'w')
                                                        
        self.boost_entry = ctk.CTkEntry(self.main_Scroll_Frame,
                                        placeholder_text = "Введите ускорение (a)",
                                        width = 420,
                                        height = 28)
        self.boost_entry.grid(column = 0, row = 4, 
                              padx = (0, 106), 
                              sticky = "e")
                                        
        self.boost_result_var = ctk.StringVar(value = "м/с²")
        self.boost_result = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                              values = ["м/с²", "км/ч²"],
                                              variable = self.boost_result_var,
                                              width = 97, height = 28,
                                              font = ctk.CTkFont(size = 20, weight = "bold"))
        self.boost_result.grid_remove()
                
        self.boost_data_var = ctk.StringVar(value = "м/с²")
        self.boost_data = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                            values = ["м/с²", "км/ч²"],
                                            width = 97,
                                            height = 28,
                                            font = ctk.CTkFont(size = 20, weight="bold"),
                                            variable = self.boost_data_var)
        self.boost_data.grid(column = 0, row = 4,
                             padx = (716, 0),
                             sticky = "w")
        
        
        
        
        # Начальная скорость                                                                    
        self.check_var_old_speed = ctk.StringVar(value="off")                            
        self.old_speed_label = ctk.CTkCheckBox(self.main_Scroll_Frame,
                                               text = 'Начальная скорость (v₀)',
                                               width=100,
                                               height=20,
                                               font = ctk.CTkFont(size = 20, weight="bold"),
                                               checkbox_width=24,
                                               checkbox_height=24,
                                               variable = self.check_var_old_speed,
                                               command = lambda:  self.old_speed_result.grid(column = 0, row = 5,
                                                                                             sticky = "w") if self.check_var_old_speed.get() == "on"
                
                                                        else self.old_speed_result.grid_remove(),
                                               onvalue = 'on',
                                               offvalue = 'off')
        self.old_speed_label.grid(column = 0, row = 5,
                                   padx = (106, 40), pady = 5, 
                                   sticky = 'w')
                 
                                                
        self.old_speed_entry = ctk.CTkEntry(self.main_Scroll_Frame,
                                            placeholder_text = 'Введите начальную скорость (v₀)',
                                            width = 310,
                                            height = 28)
        self.old_speed_entry.grid(column = 0, row = 5, 
                                  padx = (0, 106), 
                                  sticky = "e")
                
        self.old_speed_result_var = ctk.StringVar(value = 'м/с')
        self.old_speed_result = ctk.CTkOptionMenu(self.main_Scroll_Frame, values = ['м/с', 'км/ч'],
                                                  width = 97, height = 28,
                                                  variable = self.old_speed_result_var,
                                                  font = ctk.CTkFont(size = 20, weight="bold"))
        self.old_speed_result.grid_remove()
        
        self.old_speed_data_var = ctk.StringVar(value = 'м/с')
        self.old_speed_data = ctk.CTkOptionMenu(self.main_Scroll_Frame, values = ['м/с', 'км/ч'],
                                                width = 97, height = 28,
                                                variable = self.old_speed_data_var,
                                                font = ctk.CTkFont(size = 20, weight="bold"))
        self.old_speed_data.grid(column = 0, row = 5,
                                 padx = (716, 0),
                                 sticky = "w")
        
        
        
        
        
        
        # Конечная скорость                                                                                        
        self.check_var_new_speed = ctk.StringVar(value='off')                            
        self.new_speed_label = ctk.CTkCheckBox(self.main_Scroll_Frame,
                                               text = 'Конечная скорость (v)',
                                               width=100,
                                               height=20,
                                               font = ctk.CTkFont(size = 20, weight="bold"),
                                               checkbox_width=24,
                                               checkbox_height=24,
                                               command = lambda: self.new_speed_result.grid(column = 0, row = 6,
                                                                                            sticky = "w") if self.check_var_new_speed.get() == "on"
                                                     else self.new_speed_result.grid_remove(),
                                               variable = self.check_var_new_speed,
                                               onvalue = 'on',
                                               offvalue = 'off')
        self.new_speed_label.grid (column = 0, row = 6,
                                padx = (106, 40), pady = 5,
                                sticky = 'w')       
        
                                                
        self.new_speed_entry = ctk.CTkEntry(self.main_Scroll_Frame,
                                            placeholder_text = 'Введите конечную скорость (v)',
                                            width = 333,
                                            height = 28)
        self.new_speed_entry.grid(column = 0, row = 6, 
                                padx = (0, 106),
                                sticky = 'e')   
        
                
        self.new_speed_result_var = ctk.StringVar(value = 'м/с')
        self.new_speed_result = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                                  values = ['м/с', 'км/ч'],
                                                  width = 97,
                                                  height = 28,
                                                  font = ctk.CTkFont(size = 20, weight="bold"),
                                                  variable = self.new_speed_result_var)
        self.new_speed_result.grid_remove()
        
        
        self.new_speed_data_var = ctk.StringVar(value = 'м/с')
        self.new_speed_data = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                                values = ['м/с', 'км/ч'],
                                                width = 97,
                                                height = 28,
                                                font = ctk.CTkFont(size = 20, weight="bold"),
                                                variable = self.new_speed_data_var)
        self.new_speed_data.grid(column = 0, row = 6,
                                 padx = (716, 0),
                                 sticky = "w")
        
        
        
        
        
        
        # Время     
        self.check_var_time = ctk.StringVar(value='off')                            
        self.time_label = ctk.CTkCheckBox(self.main_Scroll_Frame,
                                          text = 'Время (t)',
                                          width = 100, height = 20,
                                          font = ctk.CTkFont(size = 20, weight="bold"),
                                          checkbox_width=24, checkbox_height=24,
                                          command = lambda: self.time_result.grid(column = 0, row = 7,
                                                                                  sticky = "w") if self.check_var_time.get() == "on"
                
                                                else self.time_result.grid_remove(),
                                          variable = self.check_var_time,
                                          onvalue = 'on', offvalue = 'off')
        self.time_label.grid (column = 0, row = 7,
                        padx = (106, 40), pady = 5,
                        sticky = 'w')   
                                                                                        
        self.time_entry = ctk.CTkEntry(self.main_Scroll_Frame,
                                       placeholder_text = 'Введите время (t)',
                                       width = 468,
                                       height = 28)
        self.time_entry .grid(column = 0, row = 7, 
                        padx = (0, 106),
                        sticky = 'e')   
                                        
        self.time_result_var = ctk.StringVar(value = 'с')
        self.time_result = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                             values = ['с', "мин", 'ч'],
                                             width = 97,
                                             height = 28,
                                             font = ctk.CTkFont(size = 20, weight="bold"),
                                             variable = self.time_result_var)
        self.time_result.grid_remove()
        
        self.time_data_var = ctk.StringVar(value = 'с')
        self.time_datap = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                            values = ['с', "мин", 'ч'],
                                            width = 97,
                                            height = 28,
                                            font = ctk.CTkFont(size = 20, weight="bold"),
                                            variable = self.time_data_var)
        self.time_datap.grid(column = 0, row = 7,
                        padx = (716, 0), 
                        sticky = "w") 





                                                
        # Расстояние                    
        self.check_var_distansec = ctk.StringVar(value='off')                            
        self.distans_label = ctk.CTkCheckBox(self.main_Scroll_Frame,
                                             text = 'Путь (S)',
                                             width=100,
                                             height=20,
                                             font = ctk.CTkFont(size = 20, weight="bold"),
                                             checkbox_width=24,
                                             checkbox_height=24,
                                             command = lambda: self.distans_result.grid(column = 0, row = 8,
                                                                                        sticky = "w") if self.check_var_distansec.get() == "on"
                
                                                                else self.distans_result.grid_remove(),
                                             variable = self.check_var_distansec,
                                             onvalue = 'on',
                                             offvalue = 'off')
        self.distans_label.grid (column = 0, row = 8,
                                 padx = (106, 40), pady = 5,
                                 sticky = 'w')
        self.distans_entry = ctk.CTkEntry(self.main_Scroll_Frame,
                                          placeholder_text = 'Введите путь (S)',
                                          width = 480,
                                          height = 28)
        self.distans_entry.grid(column = 0, row = 8,
                                padx = (0, 106),
                                sticky = 'e')
        self.distansec_result_var = ctk.StringVar(value = 'м')
        self.distans_result = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                                values = ['м', 'км', "см", "мм"],
                                                width = 97,
                                                height = 28,
                                                font = ctk.CTkFont(size = 20, weight="bold"),
                                                variable = self.distansec_result_var)
        self.distans_result.grid_remove()
        
        self.distans_data_var = ctk.StringVar(value ='м')
        self.distans_datap = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                               values = ['м', 'км', "см", "мм"],
                                               width = 97,
                                               height = 28,
                                               font = ctk.CTkFont(size = 20, weight="bold"),
                                               variable = self.distans_data_var)
        self.distans_datap.grid(column = 0, row = 8,
                                padx = (716, 0),
                                sticky = "w")

                    
                    
                    
                    
                                                
        # Сила приложенная к телу                                                          
        self.check_var_powerp = ctk.StringVar(value='off')                            
        self.power_at_body_label = ctk.CTkCheckBox(self.main_Scroll_Frame,
                                                   text = 'Сила приложенная к телу (F)',
                                                   width=100, height=20,
                                                   font = ctk.CTkFont(size = 20, weight="bold"),
                                                   checkbox_width=24, checkbox_height=24,
                                                   command = lambda: self.power_at_body_result.grid(column = 0, row = 9,
                                                                                                    sticky = "w") if self.check_var_powerp.get() == "on"
                
                                                                else self.power_at_body_result.grid_remove(),
                                                   variable = self.check_var_powerp,
                                                   onvalue = 'on', offvalue = 'off')
        self.power_at_body_label.grid(column = 0, row = 9,
                                      padx = (106, 40), pady = 5,
                                      sticky = 'w')
        self.power_at_body_entry = ctk.CTkEntry(self.main_Scroll_Frame,
                                                placeholder_text = 'Введите силу приложенную к телу (F)',
                                                width = 260,
                                                height = 28)
        self.power_at_body_entry.grid(column = 0, row = 9,
                                      padx = (0, 106),
                                      sticky = 'e')
        self.power_at_body_result_var = ctk.StringVar(value ='Н')
        self.power_at_body_result = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                                      values = ["МН", 'кН','Н', "мН", "мкН"],
                                                      width = 97,
                                                      height = 28,
                                                      font = ctk.CTkFont(size = 20, weight="bold"),
                                                      variable = self.power_at_body_result_var)
        self.power_at_body_result.grid_remove()
        
        self.power_at_body_data_var = ctk.StringVar(value ='Н')
        self.power_at_body_data = ctk.CTkOptionMenu(self.main_Scroll_Frame,
                                                    values = ['Н', 'кН', "МН", "мН", "мкН"],
                                                    width = 97,
                                                    height = 28,
                                                    font = ctk.CTkFont(size = 20, weight="bold"),
                                                    variable = self.power_at_body_data_var)
        self.power_at_body_data.grid(column = 0, row = 9,
                                     padx = (716, 0),
                                     sticky = "w")

                                                                
        # Масса тела                                                          
        self.check_var_mass = ctk.StringVar(value='off')                            
        self.mass_label = ctk.CTkCheckBox(self.main_Scroll_Frame,
                                          text = 'Масса тела (m)',
                                          width = 100, height = 20,
                                          onvalue = 'on', offvalue = 'off',
                                          checkbox_width = 24, checkbox_height = 24,
                                          command = lambda: self.mass_result.grid(column = 0, row = 10,
                                                                                  sticky = "w") if self.check_var_mass.get() == "on"
                
                                                        else self.mass_result.grid_remove(),
                                          variable = self.check_var_mass,
                                          font = ctk.CTkFont(size = 20, weight="bold"))
        self.mass_label.grid (column = 0, row = 10,
                        padx = (106, 40), pady = 5,
                        sticky = 'w')    
                                                                                
        self.mass_entry = ctk.CTkEntry(self.main_Scroll_Frame,
                                       placeholder_text = "Введите массу тела (m)",
                                       width = 405,
                                       height = 28)
        self.mass_entry.grid(column = 0, row = 10, 
                                padx = (0, 106),
                                sticky = "e")  
                                                                
        self.mass_result_var = ctk.StringVar(value = "кг")
        self.mass_result = ctk.CTkOptionMenu(self.main_Scroll_Frame, values = ["кг", "ц", "т", "г", "мг"],
                                             variable = self.mass_result_var,
                                             width = 97, height = 28,
                                             font = ctk.CTkFont(size = 20, weight="bold"))
        self.mass_result.grid_remove()
        
        self.mass_data_var = ctk.StringVar(value = "кг")
        self.mass_data = ctk.CTkOptionMenu(self.main_Scroll_Frame, values = ["кг", "ц", "т", "г", "мг"],
                                           variable = self.mass_data_var,
                                           width = 97, height = 28,
                                           font = ctk.CTkFont(size = 20, weight="bold"))
        self.mass_data.grid(column = 0, row = 10,
                            padx = (716, 0),
                            sticky = "w")
            
            
            
            
                                                                
        # Координаты Х                                                          
        self.check_var_coordinateX_start = ctk.StringVar(value='off')                            
        self.coordinateX_start_label = ctk.CTkCheckBox(self.main_Scroll_Frame,
                                                       text = 'Начальная координата (X₀)',
                                                       width = 100, height = 20,
                                                       onvalue = 'on', offvalue = 'off',
                                                       checkbox_width = 24, checkbox_height = 24,
                                                       variable = self.check_var_coordinateX_start,
                                                       font = ctk.CTkFont(size = 20, weight="bold"))
        self.coordinateX_start_label.grid_remove()    
                                                                                
        self.coordinateX_start_entry = ctk.CTkEntry(self.main_Scroll_Frame,
                                                    placeholder_text = "Введите начальную координату (X₀)",
                                                    width = 278, height = 28)
        self.coordinateX_start_entry.grid_remove()  
                                                                
        self.check_var_coordinateX = ctk.StringVar(value='off')                            
        self.coordinateX_label = ctk.CTkCheckBox(self.main_Scroll_Frame,
                                                 text = 'Координата (X)',
                                                 width = 100, height = 20,
                                                 onvalue = 'on', offvalue = 'off',
                                                 checkbox_width = 24, checkbox_height = 24,
                                                 variable = self.check_var_coordinateX,
                                                 font = ctk.CTkFont(size = 20, weight="bold"))
        self.coordinateX_label.grid_remove()    
                                                                                
        self.coordinateX_entry = ctk.CTkEntry(self.main_Scroll_Frame,
                                              placeholder_text = "Введите координату (X)",
                                              width = 404, height = 28)
        self.coordinateX_entry.grid_remove()  
        
        
        
        
        
        # Координаты Y                                                          
        self.check_var_coordinateY_start = ctk.StringVar(value='off')                            
        self.coordinateY_start_label = ctk.CTkCheckBox(self.main_Scroll_Frame,
                                                       text = 'Начальная координата (Y₀)',
                                                       width = 100, height = 20,
                                                       onvalue = 'on', offvalue = 'off',
                                                       checkbox_width = 24, checkbox_height = 24,
                                                       variable = self.check_var_coordinateY_start,
                                                       font = ctk.CTkFont(size = 20, weight="bold"))
        self.coordinateY_start_label.grid_remove()    
                                                                                
        self.coordinateY_start_entry = ctk.CTkEntry(self.main_Scroll_Frame,
                                                    placeholder_text = "Введите начальную координату (Y₀)",
                                                    width = 278, height = 28)
        self.coordinateY_start_entry.grid_remove()  
                                                                
        self.check_var_coordinateY = ctk.StringVar(value='off')                            
        self.coordinateY_label = ctk.CTkCheckBox(self.main_Scroll_Frame,
                                                 text = 'Координата (Y)',
                                                 width = 100, height = 20,
                                                 onvalue = 'on', offvalue = 'off',
                                                 checkbox_width = 24, checkbox_height = 24,
                                                 variable = self.check_var_coordinateY,
                                                 font = ctk.CTkFont(size = 20, weight="bold"))
        self.coordinateY_label.grid_remove()    
                                                                                
        self.coordinateY_entry = ctk.CTkEntry(self.main_Scroll_Frame,
                                              placeholder_text = "Введите координату (Y)",
                                              width = 404, height = 28)
        self.coordinateY_entry.grid_remove()  
            
            
            
                                                                
        self.Entr_data_Button = ctk.CTkButton(self, text="Вести данные",
                                              command = self.main_event,
                                              width=800, height = 100,
                                              font=ctk.CTkFont(size=60, weight="bold"),
                                              corner_radius=40)
        self.Entr_data_Button.grid(column = 0, row = 11,
                                   padx=10, pady=(30, 30))
        
        
        
        
        self.frame_result = ctk.CTkScrollableFrame(self,
                                                    width=800, height=240,
                                                    corner_radius = 20)
        self.frame_result.grid(column = 0, row = 12)
        
                                                                                                        
        self.result_label = ctk.CTkLabel(self.frame_result,
                                         text= "Ответ: ",
                                         width=40, height=28,
                                         fg_color='transparent',
                                         font=ctk.CTkFont(size = 25, weight="bold"), )
        self.result_label.grid(column = 0, row = 0)
        self.result_label.pack(anchor ="center")
        
        
            
    def main_event(self):
        try:
            result = "Ответ: "
            zero = "None"
            self.result_label.configure(text ="")
            
            distans = zero if self.distans_entry.get() == "" else self.distans_entry.get()
            old_v = zero if self.old_speed_entry.get() == "" else self.old_speed_entry.get()
            new_v = zero if self.new_speed_entry.get() == "" else self.new_speed_entry.get()
            boost = zero if self.boost_entry.get() == "" else self.boost_entry.get()
            time = zero if self.time_entry.get() == "" else self.time_entry.get()
            power = zero if self.power_at_body_entry.get() == "" else self.power_at_body_entry.get()
            mass = zero if self.mass_entry.get() == "" else self.mass_entry.get() 
            cordX = zero if self.coordinateX_entry.get() == "" else self.coordinateX_entry.get()
            cordY = zero if self.coordinateY_entry.get() == "" else self.coordinateY_entry.get()
            cordX_s = zero if self.coordinateX_start_entry.get() == "" else self.coordinateX_start_entry.get()
            cordY_s = zero if self.coordinateY_start_entry.get() == "" else self.coordinateY_start_entry.get()
            check_power = self.check_var_powerp.get()
            check_mass = self.check_var_mass.get()
            check_boost = self.check_var_boost.get()
            check_old_speed = self.check_var_old_speed.get()
            check_new_speed = self.check_var_new_speed.get()
            check_time = self.check_var_time.get()
            check_dist = self.check_var_distansec.get()
            power_at_body_data = self.power_at_body_data.get()
            power_at_body_result = self.power_at_body_result.get()
            mass_data = self.mass_data.get()
            mass_result = self.mass_result.get()
            boost_data = self.boost_data.get()
            boost_result = self.boost_result.get()
            old_speed_data = self.old_speed_data.get()
            old_speed_result = self.old_speed_result.get()
            new_speed_data = self.new_speed_data.get()
            new_speed_result = self.new_speed_result.get()
            time_data = self.time_datap.get()
            time_result = self.time_result.get()
            dist_data = self.distans_datap.get()
            dist_result = self.distans_result.get()
            height_go = self.vertical_system_combobox.get()
            check_cordX_s = self.coordinateX_start_label.get()
            check_cordX = self.coordinateX_label.get()
            check_cordY_s = self.coordinateY_start_label.get()
            check_cordY = self.coordinateY_label.get()
            coordinate_sys = self.radio_system.get()
            
            data_boost = {"м/с²": 1,
                            "км/ч²": 12960}
            
            data_speed = {"м/с": 1,
                            "км/ч": 3.6}
            
            data_time = {"с": 1,
                            "мин": 60,
                            "ч": 3600}
            
            data_distans = {"м": 1,
                            "км": 1000,
                            "см":0.01,
                            "мм":0.001}
            
            data_power = {"мкН": 0.000001,
                            "мН": 0.001, 
                            "Н": 1, 
                            "кН": 1000, 
                            "МН": 1000000}
        
            data_mass = {"мг": 0.000001, 
                            "г": 0.001, 
                            "кг": 1, 
                            "ц": 100, 
                            "т": 1000}
            
            def delta_el(array):
                el = array[0]
                for k in range(len(array) - 1):
                    el -= array[k + 1]
                return el
            
            if boost != zero: boost = delta_el(list(map(float, boost.split()))) * data_boost[boost_data]                              
            if new_v != zero: new_v = delta_el(list(map(float, new_v.split()))) / data_speed[new_speed_data]
            if old_v != zero: old_v = float(old_v) / data_speed[old_speed_data]                             
            if time != zero: time = delta_el(list(map(float, time.split()))) * data_time[time_data]
            if distans != zero: distans = float(distans) * data_distans[dist_data]
            if power != zero: power = float(power) * data_power[power_at_body_data]
            if mass != zero: mass = float(mass) * data_mass[mass_data]  
            if cordX_s != zero: cordX_s = delta_el(list(map(float, cordX_s.split())))
            if cordY_s != zero: cordY_s = delta_el(list(map(float, cordY_s.split())))
            if cordX != zero: cordX = delta_el(list(map(float, cordX.split())))
            if cordY != zero: cordY = delta_el(list(map(float, cordY.split())))

            kel = 0
            
            array_theory = []
            result_error = False
            
            while kel != 64:    
                kel += 1                                    
                result = "Ответ: "
                
                self.result_label.configure(text = "")
                
                
                if boost == zero:
                    
                    if time != zero and old_v != zero and new_v != zero: 
                        boost = (new_v - old_v) / time      
                    elif old_v != zero and new_v != zero  and distans != zero:
                        boost = (2 * (distans - old_v * time)) / (time ** 2)
                    elif old_v != zero and new_v != zero and distans != zero:
                        boost = (new_v ** 2 - old_v ** 2) / (distans * 2)
                    elif power != zero and mass != zero: 
                        boost = power / mass
                        if "nuton_two_boost" not in array_theory:
                            array_theory.append("nuton_two_boost")
                
                    if boost == zero and coordinate_sys == 2: boost = 9.8  
                    
                if old_v == zero:
                    if distans != zero and time != zero  and boost != zero:
                        old_v = (float(time) * float(boost)) / (distans * 2)
                    elif new_v != zero  and boost != zero  and time != zero: 
                        old_v = boost * time - new_v
                    elif distans != zero  and boost != zero  and new_v != zero  != zero:
                        old_v = (2 * distans * boost + (new_v ** 2)) ** 0.5
                
                if new_v == zero:
                    if distans != zero and time != zero:
                        new_v = distans / time
                    elif old_v != zero and boost != zero and time != zero: 
                        new_v = old_v + boost * time
                    elif distans != zero and boost != zero and old_v != zero:
                        new_v = (distans * 2 * boost + old_v ** 2) ** 0.5
                    elif cordX != zero and cordX_s != zero and time != zero: 
                        new_v = (cordX - cordX_s) / time
                    elif cordY != zero and cordY_s != zero and time != zero: 
                        new_v = (cordY - cordY_s) / time                   
                    
                if time == zero:
                    if distans != zero and new_v != zero:
                        time = distans / new_v
                    elif boost != zero and old_v != zero and new_v != zero: 
                        time = (new_v - old_v) / boost
                    elif boost != zero and old_v != zero and distans != zero:
                        time = (-old_v + (old_v ** 2 + 2 * boost * distans) ** 0.5) / boost
                    elif cordX != zero and cordX_s != zero and new_v != zero: 
                        time = (cordX - cordX_s) / new_v
                    elif cordY != zero and cordY_s != zero and new_v != zero: 
                        time = (cordY - cordY_s) / new_v
                                                                        
                if distans == zero:
                    if old_v != zero and boost != zero and time != zero: 
                        distans = old_v * time + (boost * (time ** 2)) / 2
                    elif new_v != zero and boost != zero and old_v != zero: 
                        distans = (new_v ** 2 - old_v ** 2) / (2 * boost)
                    elif new_v != zero and time != zero: distans = new_v * time
                    elif cordX != zero and cordX_s != zero: distans = cordX - cordX_s
                    elif cordY != zero and cordY_s != zero: distans = cordY - cordY_s    
                
                if power == zero: 
                    if zero != boost and zero != mass: 
                        power = boost * mass   
                    elif zero != time and zero != old_v and zero != new_v and zero != mass:
                        power = ((new_v - old_v) * mass) / time
                    if "nuton_two_mass" not in array_theory and power != zero:
                        array_theory.append("nuton_two_power")                                    
                
                if mass == zero:
                    if boost != zero and power != zero: 
                        mass = power / boost
                    elif zero != time and old_v and new_v and power:
                        mass = power / ((new_v - old_v) / time)
                    if "nuton_two_mass" not in array_theory and mass != zero: 
                        array_theory.append("nuton_two_mass")
                                                           
                if cordX_s == zero:
                    if cordX != zero and new_v != zero and time != zero: cordX_s = cordX - new_v * time
                    elif cordX != zero and distans != zero: cordX_s = cordX - distans
                                      
                if cordX == zero:
                    if cordX_s != zero and new_v != zero and time != zero: cordX = float(cordX_s) + new_v * time
                    elif cordX_s != zero and distans != zero: cordX = float(cordX_s) + distans
                                       
                if cordY_s == zero:
                    if cordY != zero and new_v != zero and time != zero: 
                        cordY_s = cordY - new_v * time
                    elif cordY != zero and distans != zero:
                        cordY_s = cordY - distans
                                        
                if cordY == zero:
                    if cordY_s != zero and new_v != zero and time != zero: cordY = cordY_s + new_v * time
                    elif cordY_s != zero and distans != zero: cordY = cordY_s + distans
           
                
            if boost != zero and check_boost == "on": 
                    boost = float(boost) / data_boost[boost_result]       
                    result += f"Ускорение (a) = {boost} {boost_result} \n"
            elif boost == zero and check_boost == "on":
                result_error = True
                
            if old_v != zero and check_old_speed == "on":
                    old_v = float(old_v) * data_speed[old_speed_result]
                    result += f"Начальная скорость (v₀) = {old_v} {old_speed_result} \n"
            elif old_v == zero and check_old_speed == "on":
                result_error = True
                
            if new_v != zero and check_new_speed == "on":
                    new_v = float(new_v) * data_speed[new_speed_result]
                    result += f"Скорость (v) = {new_v} {new_speed_result} \n"
            elif new_v == zero and check_new_speed == "on":
                result_error = True
                
            if time != zero and check_time == "on":
                    time = float(time) / data_time[time_result]       
                    result += f"Время (t) = {time} {time_result} \n"
            elif time == zero and check_time == "on":
                result_error = True
                
            if distans != zero and check_dist == "on":
                stated = f"{distans} {dist_result}"   
                if distans == 0: stated = f"неподвижно"
                elif distans > 0 and coordinate_sys == 2 and height_go == "вверх": stated = f"тело поднялось на {distans} {dist_result} "
                elif distans > 0 and coordinate_sys == 2 and height_go == "вниз": stated = f"тело опустилось на {distans} {dist_result} "
                elif distans < 0 and coordinate_sys == 2 and height_go == "вверх":
                    distans *= -1
                    stated = f"тело опустилось на {distans} {dist_result} "
                elif distans < 0 and coordinate_sys == 2 and height_go == "вниз":
                    distans *= -1
                    stated = f"тело поднялось на {distans} {dist_result} "
                distans = float(distans) * data_distans[dist_result]
                result += f"Расстояние (S) = {stated}\n"
            elif distans == zero and check_dist == "on":
                result_error = True
                
            if power != zero and check_power == "on": 
                    power = float(power) * data_power[power_at_body_result]
                    result += f"Сила (F) = {power} {power_at_body_result} \n"
            elif power == zero and check_power == "on":
                result_error = True
                
            if mass != zero and check_mass == "on": 
                    mass = float(mass) / data_mass[mass_result]
                    result += f"Масса (m) = {mass} {mass_result} \n"
            elif mass == zero and check_mass == "on":
                result_error = True
                
            if cordX_s != zero and check_cordX_s == "on":result += f"Начальная точка (X₀) = {cordX_s}\n"
            elif cordX_s == zero and check_cordX_s == "on": result_error = True
            
            if cordX != zero and check_cordX == "on": result += f"Точка (X) = {cordX}\n"
            elif cordX == zero and check_cordX == "on":result_error = True
           
            if cordY_s != zero and check_cordY_s == "on": result += f"Начальная точка (Y₀) = {cordY_s}\n"
            elif cordY_s == zero and check_cordY_s == "on":result_error = True
            
            if cordY != zero and check_cordY == "on": result += f"Точка (Y) = {cordY}\n"
            elif cordY == zero and check_cordY == "on": result_error = True
            
            theory = {'nuton_two_boost': "\n\tВторой закон Ньютона \nСогласно второму закону Ньютона ускорение тела\n прямо пропорционально равнодействующей сил, "
                                                           "\nприложенных к телу, и обратно пропорционально его массе. \nИз чего следует что a = F/m",
                      'nuton_two_power': "\n\tВторой закон Ньютона \nСогласно второму закону Ньютона ускорение тела прямо пропорционально равнодействующей сил, "
                                                           "\nприложенных к телу, и обратно пропорционально его массе. Из чего следует что F = m * a",
                      'nuton_two_mass': "\n\tВторой закон Ньютона \nСогласно второму закону Ньютона ускорение тела прямо пропорционально равнодействующей сил, "
                                                           "\nприложенных к телу, и обратно пропорционально его массе. Из чего следует что m = F / a "}
            
            for k in array_theory:
                result += theory[k]
            if result_error: result = "Недостаточно данных \nили данные некорректны"  
            result_error = False        
            self.result_label.configure(text = result)
            
        except ValueError:
            result = "Недостаточно данных \nили данные некорректны"
            self.result_label.configure(text = result)
        
                                            
    def show_openMenu_Y(self):
        self.vertical_system_combobox.grid(column = 0, row = 0,
                                           padx = (0, 5), pady = 0,
                                           sticky = 'e')
        self.horizontal_system_combobox.grid_remove()
        
        self.coordinateY_start_label.grid (column = 0, row = 11,
                                           padx = (106, 40), pady = 5, 
                                           sticky = 'w')
        
        self.coordinateY_start_entry.grid(column = 0, row = 11, 
                                          padx = (0, 106), 
                                          sticky = "e")
        
        self.coordinateY_label.grid (column = 0, row = 12,
                                     padx = (106, 40), pady = 5, 
                                     sticky = 'w')
        
        self.coordinateY_entry.grid(column = 0, row = 12, 
                                    padx = (0, 106), 
                                    sticky = "e")  
        
        self.coordinateX_entry.grid_remove()
        self.coordinateX_label.grid_remove()
        self.coordinateX_start_entry.grid_remove()
        self.coordinateX_start_label.grid_remove()
        self.coordinateX_label.deselect()
        self.coordinateX_start_label.deselect()                               
    
    def show_openMenu_X(self):
        self.vertical_system_combobox.grid_remove()
        
        self.coordinateX_start_label.grid (column = 0, row = 11,
                                           padx = (106, 40), pady = 5, 
                                           sticky = 'w') 
        
        self.coordinateX_start_entry.grid(column = 0, row = 11, 
                                          padx = (0, 106), 
                                          sticky = "e") 
        
        self.coordinateX_label.grid (column = 0, row = 12,
                                     padx = (106, 40), pady = 5, 
                                     sticky = 'w')       
        
        self.coordinateX_entry.grid(column = 0, row = 12, 
                                    padx = (0, 106), 
                                    sticky = "e") 
        
        self.coordinateY_entry.grid_remove()
        self.coordinateY_label.grid_remove()
        self.coordinateY_start_entry.grid_remove()
        self.coordinateY_start_label.grid_remove()
        self.coordinateY_label.deselect()
        self.coordinateY_start_label.deselect()
    
    def pram_move_event(self):
        self.boost_label.grid(column = 0,row = 4,
                              padx = (106, 40), pady = 5, 
                              sticky = 'w')
        
        self.boost_entry.grid(column = 0, row = 4, 
                              padx = (0, 106), 
                              sticky = "e")
        
        self.boost_data.grid(column = 0, row = 4,
                             padx = (716, 0),
                             sticky = "w")
        
        self.old_speed_label.grid(column = 0, row = 5,
                                   padx = (106, 40), pady = 5, 
                                   sticky = 'w')
        
        self.old_speed_entry.grid(column = 0, row = 5, 
                                  padx = (0, 106), 
                                  sticky = "e")
        
        self.old_speed_data.grid(column = 0, row = 5,
                                 padx = (716, 0),
                                 sticky = "w")
                    
    def boost_move_event(self):
        self.boost_label.grid_remove()
        self.boost_entry.grid_remove()
        self.boost_data.grid_remove()
        self.boost_result.grid_remove()
        self.old_speed_label.grid_remove()
        self.old_speed_entry.grid_remove()
        self.old_speed_data.grid_remove()
        self.old_speed_result.grid_remove()



app = App()
app.mainloop()
