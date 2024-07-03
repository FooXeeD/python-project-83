### Hexlet tests and linter status:
[![Actions Status](https://github.com/FooXeeD/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/FooXeeD/python-project-83/actions)
[![all tests](https://github.com/Barzabel/python-project-83/workflows/all_tests/badge.svg)](https://github.com/FooXeed/python-project-83/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/8d93f5f8033ec513a8fd/maintainability)](https://codeclimate.com/github/FooXeeD/python-project-83/maintainability)

# Анализатор страниц

Анализатор страниц – это сайт, который анализирует указанные страницы на SEO-пригодность по аналогии с PageSpeed Insights:

### Проверить работу анализатора можно [тут](https://python-project-83-xakg.onrender.com/)

## Установка
* Скопируйте репозиторий: 
```git clone https://github.com/FooXeeD/python-project-83```.
Вам необходимо указать данные для подключения к базе данных `$DATABASE_URL` and `$SECRET_KEY` vars.

Для запуска создайте файл `.env` в корневом каталоге. 
Измените значения `SECRET_KEY` м `DATABASE_URL.` на свои.

Команда ```make build``` установит необходимые пакеты и создаст базу данных.

Команда ```make start``` запуститcя сервер. Анализатор сайтов будет доступен по адресу: http://localhost:8000/