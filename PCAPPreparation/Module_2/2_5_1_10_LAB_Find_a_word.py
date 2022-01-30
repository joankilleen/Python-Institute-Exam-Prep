'''Find a word Lab Modukle 2'''

word=""
text =""
success=True
while True:
    while word=="":
        word=input("Enter the word to seach for...: ")
    while text=="":
        text=input("..in this piece of text: ")
    next_index=0
    for ch in word:
        next_index = text.find(ch, next_index)
        if next_index == -1:
            print("Character not found: ", ch)
            success=False
            break
        else:
            print(f"Character {ch} found at index {next_index}")
    print("Success? ", success)
    word=""
    text =""


