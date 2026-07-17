import string

print("Диапазон букв!\n")

input_chars = input("Введите через дефис две буквы (a-z, A-Z): ")

if (
    len(input_chars) != 3
    or input_chars[1] != '-'
    or input_chars[0] not in string.ascii_letters
    or input_chars[2] not in string.ascii_letters
):
    print("Некоректный ввод!")
else:
    letters = string.ascii_letters

    start_char = letters.index(input_chars[0])
    end_char = letters.index(input_chars[2])

    if start_char <= end_char:
        print(letters[start_char:end_char + 1])
    else:
        print("Некоректный ввод!")