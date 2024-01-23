from tkinter import *
from tkinter import filedialog 
import binary2strings as b2s
import os

def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "~", 
                                          title = "Selecionar arquivo", 
                                          filetypes = (("Bios files", 
                                                        ("*.bin", "*.rom")), 
                                                       ("all files", 
                                                        "*.*"))) 
    
    if not filename:
        label_file_explorer.configure(text="Cancelado", fg = "red", font='Helvetica 12 bold')
    else:
         label_file_explorer.configure(text="Arquivo aberto: "+filename, fg = "blue", font='Helvetica 12 bold')
         ok = 0
         with open(filename, "rb") as i:
            data = i.read()
            for (string, type, span, is_interesting) in b2s.extract_all_strings(data, min_chars=29):

                if len(string) == 29 and string[5] == '-' and string[11 == '-'] and string[17] == '-' and string[23] == '-':
                    ok = 1
                    chave = string
            if ok == 1:
               label_file_explorer.configure(text=f'\nO serial encontrado no arquivo é:\n{chave}', fg = "blue", font='Helvetica 12 bold')
            else:
               label_file_explorer.configure(text='\nNenhum serial encontrado no arquivo.', fg = "red", font='Helvetica 12 bold')

window = Tk() 
window.title('Winkey - by ACL') 
#window.geometry("500x500") 
#window.config(background = "white") 
   
label_file_explorer = Label(window,  
                            text = ("Windows key Recover\nPor favor, selecione um arquivo."), 
                            width = 50, height = 4,  
                            fg = "black",
                            font='Helvetica 12 bold') 
   
       
button_explore = Button(window,  
                        text = "Selecionar arquivo", 
                        command = browseFiles)  
   
button_exit = Button(window,  
                     text = "Sair", 
                     command = exit)  
   
label_file_explorer.grid(column = 1, row = 1) 
button_explore.grid(column = 1, row = 2) 
button_exit.grid(column = 1,row = 3) 
window.mainloop()

