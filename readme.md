# turueee_bot

Данный проект - telegram-бот-помошник.
Он имеет две кнопки:

1. Конвертер валют - вызывает функцию, которая переводит заданную сумму денег из одной валюты в другую по текущему курсу.
2. Погода - вызывает функцию, которая показывает температуру, в заданном месте.

## Активация бота

1. Скачать все файлы из репозитория.
2. Установить библиотеки, перечисленные в requirements.txt.
3. Получить секретный ключ и API-ключ на сайте https://dadata.ru/profile/#info.
4. Получить токен бота от BotFather.
5. Создать файл .env и заполнить его (API_TOKEN='токен бота', TOKEN = 'API-ключ от Dadata', SECRET='секретный ключ от Dadata')
6. Запустить файл main.py.

## Как работать

1. Введите команду '/start', ознакомьтесь с инструкцией, которую выдаст бот.
2. Введите команду 'Погода' или 'Конвертер валют'.
3.
    1. Если введена команда 'Погода', то далее введите адрес (пример: нижний новгород краснодонцев 15).
    2. Если введена команда 'Конвертер валют', то введите сумму денег, код валюты этой суммы денег и код валюты, в которую нужно
       перевести данную сумму (пример: 100 USD RUB).
   3. Примечание, бот выполняет команду, пока не будет дана новая.