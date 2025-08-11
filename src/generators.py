def filter_by_currency(transactions, currency):
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    counter_currency = 0
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            counter_currency += 1
            yield transaction
    if counter_currency == 0:
        yield []


def transaction_descriptions(transactions):
    """Функция возвращает описание каждой операции по очереди"""
    if transactions:
        for transaction in transactions:
            result_transactions = transaction.get("description")
            yield result_transactions
    else:
        yield []


def card_number_generator(start, stop):
    """Генерирует номера карт в заданном диапазоне"""
    for number in range(start, stop):
        card_number = str(number).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"