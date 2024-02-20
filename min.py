def is_palindrome(word):
    word = word.lower()

    return word == word[::-1]

def main():
    user_input = input("Введіть слово: ")

    if is_palindrome(user_input):
        print("Це слово - паліндром!")
    else:
        print("Цеслово неє паліндромом.")

if __name__ == "__main__":
    main()    