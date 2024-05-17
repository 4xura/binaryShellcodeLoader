#!/bin/bash

# Extract the base name without extension
base_name=$(basename "$1" .asm)

echo '[+] Assembling with Nasm …'
nasm -f elf64 "$base_name.asm" -o "$base_name.o"

echo '[+] Linking …'
ld "$base_name.o" -o "$base_name"

echo '[+] Extracting hex …'
objcopy -O binary -j .text "$base_name" "$base_name.bin"

echo '[+] Converting into byte format …'
xxd -p "$base_name.bin" | tr -d '\n' | sed 's/\(..\)/\\x\1/g' > "$base_name.txt"

echo '[+] Done!'

