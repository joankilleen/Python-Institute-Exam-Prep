from os import strerror

character_frequencies = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rt')
    buffer = src.read(1000)
    while buffer != '':
        buffer = buffer.lower()
        for ch in buffer:
            if not ch.isalpha():
                continue          
            character_frequencies[ch] += 1
        buffer = src.read(1000)
    src.close()
    for ch in character_frequencies:
        if  character_frequencies[ch] > 0:
            print(ch, "->", character_frequencies[ch])
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	