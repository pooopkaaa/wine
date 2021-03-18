# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка

- Скачайте код
- Установите зависимости для работы с проектом pip install -r requirements.txt

## Запуск

- Запустите сайт командой `python3 main.py` использую файл с продукцией по умолчанию `wine.xlsx`
- Запустите сайт командой `python3 main.py -f example.xlsx` используя свой файл с продукцией `example.xlsx`
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Настройка

- Сформируйте свой файл с продукцией `example.xlsx`, используя файл по умолчанию `wine.xlsx`
- Файл должен иметь расширение `xlsx` или `xls`
- Изображение продукции размещаются в папке `images`
- Наименование заголовков столбцов файла не изменяется:

Категория | Название | Сорт | Цена | Картинка | Акция
--------- | -------- | ---- | ---- | -------- | -----

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
