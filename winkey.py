#!/bin/bash
import binary2strings as b2s
import os

ok = 0
arquivo = input('\nQual o nome do arquivo? ')
if os.path.isfile(arquivo):
        with open(arquivo, "rb") as i:
            data = i.read()
            for (string, type, span, is_interesting) in b2s.extract_all_strings(data, min_chars=29):

                if len(string) == 29 and string[5] == '-' and string[11 == '-'] and string[17] == '-' and string[23] == '-':
                    ok = 1
                    chave = string
            if ok == 1:
                print('\nO serial encontrado no arquivo é:')
                print(f'\n\033[1;33m{chave}\n')
            else:
                print('\033[1;33m\nChave inexistente neste arquivo\n')
else:
    print('\033[1;31m\nArquivo inválido.\n')

