def mysplit(strng):
    input_array = list(strng)
    #
    WHITESPACE = ' '
    output = []
    next_split_index = 0
    i=0
    while i < len(strng):
        char = strng[i]     
        if char == WHITESPACE:
            str_to_append = strng[next_split_index: i]
            if str_to_append:
                output.append(str_to_append)
            next_split_index = i+1
        i+=1
    return output
            
        


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
