import os

import pytest

from src.decorators import log


@log()
def my_function(x, y):
    return x / y


# Проверка на успешное выполнение функции


def test_my_function_success(capsys):
    result = my_function(4, 2)
    assert result == 2
    captured = capsys.readouterr()
    assert "my_function ок. Результат: 2" in captured.out


# Проверка обработки исключений


def test_my_function_division_by_zero(capsys):
    my_function(4, 0)
    captured = capsys.readouterr()
    assert "my_function error: division by zero. Inputs: (4, 0), {}" in captured.out


@log()
def my_function_key_error():
    return {"a": 1}["b"]


def test_my_function_key_error(capsys):
    my_function_key_error()
    captured = capsys.readouterr()
    assert "my_function_key_error error: 'b'. Inputs: (), {}" in captured.out


# Проверка на вывод в файл


@log(filename="test_log.txt")
def my_function_sum(x, y):
    return x + y


def test_my_function_file_output():
    my_function_sum(2, 3)
    with open("test_log.txt", "r", encoding="utf-8") as file:
        content = file.read()
    assert "Функция my_function_sum ок. Результат: 5" in content
    os.remove("test_log.txt")


# Проверка с другими типами аргументов


@log()
def my_function_concat(a, b):
    return a + b


def test_my_function_concat_strings(capsys):
    result = my_function_concat("hello", "world")
    assert result == "helloworld"
    captured = capsys.readouterr()
    assert "my_function_concat ок. Результат: helloworld" in captured.out
