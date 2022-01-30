'''Testing Anagrams'''
str_1 = ""
str_2 = ""
while True:
    while str_1 == "":
        str_1 = input("Enter the first string: ").lower().replace(" ", "")
    while str_2 == "":
        str_2 = input("Enter the first string: ").lower().replace(" ", "")
    is_anagram = True
    if len(str_1) != len(str_2):
        is_anagram = False
    else:
        for ch in str_1:
            if ch  not in str_2:
                is_anagram = False
                break
    print("Are they anagrams? ", is_anagram)
    str_1 = ""
    str_2 = ""

