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
Пример использования функций:
```
from src.masks import get_mask_card_number

number_card = '7000792289606361'

result = get_mask_card_number(number_card)
```

