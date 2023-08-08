# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

from random import choice


def get_jokes(n: int) -> list[str]:
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []
    for i in range(n):
        # joke = choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
        joke = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        jokes_list.append(joke)

    return jokes_list


print(get_jokes(5))
