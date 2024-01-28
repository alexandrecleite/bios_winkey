#!/usr/bin/python
import PySimpleGUI as sg 
import sys, re   

def engine(arquivo):
   with open(arquivo, 'rb') as f:
       s = f.read()
       for match in re.finditer(b'\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x1d\x00\x00', s):
           pos = match.span()
           f.seek(pos[1])
           result = str(f.read(30))
           serialnum = 'A chave de ativação é:', result[6:35]
           return serialnum

sg.theme('BlueMono') 
   
layout = [[sg.Text('Por favor, selecione o arquivo:'), 
           sg.Text(size=(15,1), key='-OUTPUT-')], 
          [sg.Input(), sg.FileBrowse(button_text="Selecionar", file_types=(("Bios Files", "*.bin *.rom"),("All Files", "*.*")))],
          [sg.Button('Verificar'), sg.Button('Sair')]]
  
window = sg.Window('WINKEY v2 - by ACL', layout) 
  
while True: 
    event, values = window.read() 
      
    if event in  (None, 'Sair'): 
        break
      
    if event == 'Verificar': 
        arquivo = values[0] 
        if arquivo == "" or engine(arquivo) == None:
            sg.popup('Chave não encontrada.\nPor favor, selecione outro arquivo.', font=('Arial 10 bold'))
        else:
#                print(engine(arquivo))
                arquivo = values[0]
                sg.popup(font=('Arial 10 bold'), text_color=('blue'), *engine(arquivo))

window.close()

