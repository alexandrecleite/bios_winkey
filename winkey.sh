#!/usr/bin/env bash
#Autor: Alexandre C. Leite
#Data: 06/08/2024
# Script para extrair o serial de um arquivo de BIOS UEFI.

# Verifica se o arquivo foi passado como argumento
if [ $# -ne 1 ]; then
    echo "Uso: $0 <arquivo>"
    exit 1
fi

# Define o padrão a ser buscado
padrao="010000000000000001000000000000001d0000"

# Converte o padrão para uma expressão regular hexadecimal
hex_padrao=$(echo $padrao | sed 's/ /\\x/g')

# Encontra a posição do padrão no arquivo
offset=$(xxd -p "$1" | tr -d '\n' | grep -aob "$hex_padrao" | cut -d: -f1)

# Verifica se o padrão foi encontrado
if [ -z "$offset" ]; then
    echo "Serial não encontrado."
    exit 1
fi

# Converte o offset para bytes
byte_offset=$((offset / 2 + ${#hex_padrao} / 4))

# Lê e imprime os próximos 30 bytes em ASCII
echo
echo "O serial é:"
echo
dd if="$1" bs=1 skip="$byte_offset" count=40 2>/dev/null | xxd -p | while read -r line; do
    echo "$line" | xxd -r -p
done
echo;echo
