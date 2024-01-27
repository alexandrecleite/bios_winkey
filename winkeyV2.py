#!/usr/bin/python
import sys, re

if len(sys.argv) < 2:
    print('\nVocê deve especificar o nome do arquivo. Ex: "\33[1;33mpython winkey.py bios.bin\33[0;40m"\n')
    sys.exit()

with open(sys.argv[1], 'rb') as f:
    s = f.read()
    for match in re.finditer(b'\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x1d\x00\x00\x00', s):
        pos = match.span()
        f.seek(pos[1])
        result = str(f.read(29))
print('\nA chave de ativação é:\33[1;33m ', result[2:31],'\n\33[0;40m')

