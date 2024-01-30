'''
Created on Dec 26, 2023

@author: andri
'''
import tkinter as tk 
from tkinter import StringVar






if __name__ == '__main__':
    wn = tk.Tk()
    wn.title("Calculator")
    
    origin_frame = tk.LabelFrame(wn, text = "")
    origin_frame.grid(row = 0, column = 0, padx = 5, pady = 5)
    
    display_box = StringVar 
    display_boxx = tk.Entry(origin_frame, textvariable= display_box, width = 28, font = ("Times New Roman", 15))
    display_boxx.grid(row = 0, column = 0, padx = 5, pady = 5, columnspan = 3)
    ## Number Buttons ## 
    number_1 = tk.Button(origin_frame, text = "1", width = 9, font = ("Times New Roman", 13))
    number_1.grid(row = 1, column = 0, padx = 5, pady = 5)
    
    number_2 = tk.Button(origin_frame, text = "2", width = 9, font = ("Times New Roman", 13))
    number_2.grid(row = 1, column = 1, padx = 5, pady = 5)
    
    number_3 = tk.Button(origin_frame, text = "3", width = 9, font = ("Times New Roman", 13))
    number_3.grid(row = 1, column = 2, padx = 5, pady = 5)
    
    number_4 = tk.Button(origin_frame, text = "4", width = 9, font = ("Times New Roman", 13))
    number_4.grid(row = 2, column = 0, padx = 5, pady = 5)
    
    number_5 = tk.Button(origin_frame, text = "5", width = 9, font = ("Times New Roman", 13))
    number_5.grid(row = 2, column = 1, padx = 5, pady = 5)
    
    number_6 = tk.Button(origin_frame, text = "6", width = 9, font = ("Times New Roman", 13))
    number_6.grid(row = 2, column = 2, padx = 5, pady = 5)
    
    number_7 = tk.Button(origin_frame, text = "7", width = 9, font = ("Times New Roman", 13))
    number_7.grid(row = 3, column = 0, padx = 5, pady = 5)
    
    number_8 = tk.Button(origin_frame, text = "8", width = 9, font = ("Times New Roman", 13))
    number_8.grid(row = 3, column = 1, padx = 5, pady = 5)
    
    number_9 = tk.Button(origin_frame, text = "9", width = 9, font = ("Times New Roman", 13))
    number_9.grid(row = 3, column = 2, padx = 5, pady = 5)
    
    number_1 = tk.Button(origin_frame, text = "0", width = 9, font = ("Times New Roman", 13))
    number_1.grid(row = 4, column = 1, padx = 5, pady = 5)
    
    ## Symbols and Clear Button## 
    
    symbol_x = tk.Button(origin_frame, text = "x", width = 9, font = ("Times New Roman", 13))
    symbol_x.grid(row = 0, column = 3, padx = 5, pady = 5)
    
    symbol_l = tk.Button(origin_frame, text = "/", width = 9, font = ("Times New Roman", 13))
    symbol_l.grid(row = 1, column = 3, padx = 5, pady = 5)
    
    symbol_t = tk.Button(origin_frame, text = "+", width = 9, font = ("Times New Roman", 13))
    symbol_t.grid(row = 2, column = 3, padx = 5, pady = 5)
    
    symbol_ = tk.Button(origin_frame, text = "-", width = 9, font = ("Times New Roman", 13))
    symbol_.grid(row = 3, column = 3, padx = 5, pady = 5)
    
    clear = tk.Button(origin_frame, text = "Clear", width = 9, font = ("Times New Roman", 13))
    clear.grid(row = 4, column = 2, padx = 5, pady = 5)
    
    close = tk.Button(origin_frame, text = "Close", width = 9, font = ("Times New Roman", 13))
    close.grid(row = 4, column = 3, padx = 5, pady = 5)
    
    
    
    
    
    
    
   
   
   
   
   
    wn.mainloop()