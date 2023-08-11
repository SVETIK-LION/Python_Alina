from decimal import Decimal
import requests


def get_currency_rates(code: str) -> Decimal | str:
    """
    Получить значение по кодовому названию валюты
    :param code: код валюты
    :return: значение валюты
    """
    with open('request_cbr.txt', 'w') as file_value, open('result.txt', 'a') as result_file:
        r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        values_list = r.text.split('</Valute>')
        for i in range(len(values_list)):
            values_list[i] = values_list[i]+'\n'

        file_value.writelines(values_list)
        flag = False
        for i in range(len(values_list)):
            if code.upper() in values_list[i]:
                flag = True
                new_str = values_list[i].replace('</Value>', '<Value>')
                new_list = new_str.split('<Value>')

                result = Decimal(new_list[-2].replace(',', '.'))
                result_file.write(str(result) + '\n')
    if not flag:
        return f'Валюты {code} нет.'
    return result


print(get_currency_rates("usd"))
print(get_currency_rates("noname"))
