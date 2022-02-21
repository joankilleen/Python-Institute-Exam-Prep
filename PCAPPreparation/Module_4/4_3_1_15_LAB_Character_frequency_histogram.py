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
    filtered_chars= dict(filter(lambda item: item[1] > 0, character_frequencies.items()))
    sorted_chars= dict(sorted(filtered_chars.items(), key=lambda item: item[1], reverse=True))
    dest=open(srcname+'.hist', 'wt')
    for item in sorted_chars.items():
        dest.write(str(item[0]) + "->"  + str(item[1]) + '\n')
    dest.close()
    print(sorted_chars)

except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	