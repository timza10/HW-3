word = 'char'
previous_char = None
while True:
    char = input("Enter the word:")
    if char == previous_char:
        print("No sequential duplicates allowed , you've entered:", word)
        break
    word += char
    previous_char = char