# Написать функцию `num_translate()`, переводящую числительные от `0` до `10` c английского на русский язык.

# Если перевод сделать невозможно, вернуть `None`.

# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


def num_translate(num: str) -> str | None:
    numbers = {"zero": "ноль",
               "one": "один",
               "two": "два",
               "tree": "три",
               "four": "четыре",
               "five": "пять",
               "six": "шесть",
               "seven": "семь",
               "eight": "восемь",
               "nine": "девять",
               "ten": "десять"}
    num = num.lower()
    if num in numbers:
        return numbers[num]
    else:
        return None

num = input("Введите число на английском от 0 до 10: ")
print(num_translate(num))
