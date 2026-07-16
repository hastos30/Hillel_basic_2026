import re
import string
import keyword

print("Проверка, может ли введенный текст быть именем переменной")

message = input("Введите текст: ")

if (
    re.search(r"_{2,}", message) 
    or re.search(r"\s", message)
    or any(char in string.punctuation.replace("_", "") for char in message)
    or any(char.isupper() for char in message)
    or (message and message[0].isdigit())
    or message in keyword.kwlist
    or any(char not in string.ascii_lowercase + string.digits + "_" for char in message)
):
    print(False)
else:
    print(True)