import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date
from tests.conftest import input_data


# Функция filter_by_state
# Тестирование фильтрации списка словарей по заданному статусу state
def test_filter_by_state(input_data):
    assert filter_by_state(input_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
def test_filter_by_state(input_data):
    assert filter_by_state(input_data, state="HELLO") == []


# Тестирование фильтрации списка словарей по другому заданному статусу state, существующему в списке словарей
def test_filter_by_state(input_data):
    assert filter_by_state(input_data, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Функция sort_by_date
# Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
def test_sort_by_date(input_data):
    assert sort_by_date(input_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date(input_data):
    assert sort_by_date(input_data, reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


# Тесты на работу функции с некорректными или нестандартными форматами дат.
def test_sort_by_date():
    assert (
        sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-14-03T18:35:29.512364"}])
        == "Неверный формат даты"
    )


def test_sort_by_date():
    assert (
        sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "14-03-2019T18:35:29.512364"}])
        == "Неверный формат даты"
    )
