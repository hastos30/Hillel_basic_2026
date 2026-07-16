import string

print("Программа переобразования текста в hashtag")

message = input("Введите текст: ")

message = message.translate(str.maketrans("", "", string.punctuation))
message = message.title()
message = message.replace(" ", "")

message = "#" + message

message = message[:140]

print(message)