print("Конвертер из числа в дату!\n")

input_seconds = int(input("Введите количество секунд (0 - 8640000):"))

days_in_seconds = 24 * 60 * 60
hours_in_seconds = 60 * 60
minutes_in_seconds = 60

if input_seconds < 0 or input_seconds >= 8640000:
    print("Ошибка: некорректный ввод числа")
else:
    # days = input_seconds // days_in_seconds
    # hours = (input_seconds - (hours_in_seconds * 24 * days)) // hours_in_seconds
    # minutes = (input_seconds - (hours_in_seconds * 24 * days) - (hours_in_seconds * hours)) // minutes_in_seconds
    # seconds = (input_seconds - (hours_in_seconds * 24 * days) - (hours_in_seconds * hours) - (minutes_in_seconds * minutes))

    # days = input_seconds // days_in_seconds
    # hours = input_seconds % days_in_seconds // hours_in_seconds
    # minutes = input_seconds % hours_in_seconds // minutes_in_seconds
    # seconds = input_seconds % minutes_in_seconds

    days, remainder = divmod(input_seconds, days_in_seconds)
    hours, remainder = divmod(remainder, hours_in_seconds)
    minutes, remainder = divmod(remainder, minutes_in_seconds)
    seconds, remainder = divmod(remainder, 1)

    print(f"{days} дней, {hours:02}:{minutes:02}:{seconds:02}")