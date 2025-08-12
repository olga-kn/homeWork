# Банковские операции 
## Описание:
Проект работает с банковскими операциями, позволяя маскировать номера карт и счетов, фильтровать и сортировать транзакции.
## Установка:
1. Клонируйте репозиторий:
```
git clone https://github.com/olga-kn/homeWork.git
```
2. Установите зависимости:
```
poetry install 
```
## Использование:

Описание и пример использования функций:

1. Модуль masks

Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску

Пример использования функций:
```
from src.masks import get_mask_card_number

number_card = '7000792289606361'
result = get_mask_card_number(number_card)
```
Функция get_mask_account принимает на вход номер счета и возвращает его маску.

Пример использования функций:
```
from src.masks import get_mask_account

account_number = '73654108430135874305'
result = get_mask_account(account_number)
```
2. Модуль widget

Функция mask_account_card принимает один аргумент — строку, содержащую тип и номер карты или счета, возвращает строку с замаскированным номером.

Пример использования функций:
```
from src.widget import mask_account_card

info_card = 'Maestro 1596837868705199'
result = mask_account_card(info_card)
```
Функция get_date принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате 
"ДД.ММ.ГГГГ"

Пример использования функций:
```
from src.widget import get_date

date_str = "2024-03-11T02:26:18.671407"
result = get_date(date_str)
```
3. Модуль processing

Функция filter_by_state принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
 соответствует указанному значению.

Пример использования функций:
```
from src.processing import filter_by_state

list_of_dic = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
result = filter_by_state(list_of_dic, state = "EXECUTED")
```
Функция sort_by_date принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция возвращаtn новый список, отсортированный по дате (date)

Пример использования функций:
```
from src.processing import sort_by_date

list_of_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
result = sort_by_date(list_of_dict, reverse = True)
```
4. Модуль generators

Функция filter_by_currency принимает на вход список словарей, представляющих транзакции, возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной

Пример использования функций:
```
from src.generators import filter_by_currency

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
```
Генератор transaction_descriptions принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

Пример использования функций:
```
from src.generators import transaction_descriptions

# Входные данные используем те что указанны в функции filter_by_currency
descriptions = transaction_descriptions(transactions) 
for _ in range(5):
    print(next(descriptions))
```
Генератор card_number_generator выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Генератор  принимает начальное и конечное значения для генерации диапазона номеров.

Пример использования функций:
```
from src.generators import transaction_descriptions

for card_number in card_number_generator(1, 5):
    print(card_number)
```
5. Модуль decorators

Декоратор log автоматически регистрирует детали выполнения функций, такие как время вызова, имя функции, передаваемые аргументы, результат выполнения и информация об ошибках.

Пример использования декоратора:

``` 
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(8, 2)
```
## Тестирование:
1. Для тестирования используется библиотека pytest.

2. Запустить тесты можно используя команду pytest.

3. Код покрыт тестами на 90%, есть отчет в формате HTML в папке htmlcov, файл index.html.

