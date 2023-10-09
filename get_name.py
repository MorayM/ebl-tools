import sys

file_name = sys.argv[1]

f = open(file_name, 'rb') # open in binary mode
f.seek(34, 0) # shift to 34 bytes from the start of the file
raw_name = f.read(28) # read 28 bytes
f.close()
name = raw_name.replace(b'\x00', b'').decode('ascii') # raw_name is a binary string
print(name)
