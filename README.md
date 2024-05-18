# binaryShellcodeLoader

Recently, I have a demmand for encoding a Linux-cmd-64bit shellcode to bypass some security checks. There are a lot shellcode loaders for Windows machine to generate an executable to run, but rarely for the elf binary in Linux Systyem. So I make a simple framework that allow us to encode the shellcode, and auto generates the final binary with both decoder & shellcode.

We can add more procedures for the Encoder & Decoder respectivly when we need to bypass complicate AV or security checks. And this Encoder & Decoder is easy to use with following steps:

1. Place the *desired shellcode* into the XOR Encoder `shellcode_generator.py`, and run it to generate an *encoded shellcode*.
2. Paste *encoded shellcode* into the Assembly Decoder `decoder.asm`.
3. Use the bash script `./compile.sh decoder.asm` to print out the final *obfuscated shellcode*.
4. The final *obfuscated shellcode* locates at `.txt` file. Use it and exploit.

5. For more details read: https://4xura.com/pwn/create-a-shellcode-encoder-for-binary-exploit/
