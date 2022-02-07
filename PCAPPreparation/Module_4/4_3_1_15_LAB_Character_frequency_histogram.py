from os import strerror

character_frequencies = {}
srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rt')
    buffer = src.read(1000)
    while buffer != '':
        buffer = buffer.lower()
        for ch in buffer:
            #if not str(ch).isalpha():
            #    continue
            ch_exists = ch in character_frequencies
            if (ch_exists):
                character_frequencies[ch] += character_frequencies[ch]
            else:
                character_frequencies[ch] = 1
        buffer = src.read(1000)
    src.close()
    for ch in character_frequencies:
        print(ch, "->", character_frequencies[ch])
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	