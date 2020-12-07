# Пульт управления для охраника банка

Это репозиторий в котором храниться приложение для охранников хранилища. В приложении выводиться информация: история посещений хранилища, проведенное время, и система распозонавания подозрительных посещений. Так же встроена система показа сотрудников, которые находятся в хранилище прямо сейчас

### Как установить

Переименйуте файл `project/env.sample` в `.env`. Укажите необходимые ключи:

|Ключ           |Описание|Пример|
|---------------|--------|------|
|`DB_HOST`      |Хост БД|db.example.org|
|`DB_PORT`      |Порт БД|5434|
|`DB_NAME`      |Имя БД|checkpoint|
|`DB_USER`      |Пользователь БД|root|
|`DB_PASSWORD`  |Пароль БД|root|
|`SECRET_KEY`   |Секретный ключ для Django ([подробнее](https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key))|secret-example|
|`LANGUAGE_CODE`|Язык локализации Django ([подробнее](https://docs.djangoproject.com/en/3.1/ref/settings/#language-code))|ru-ru|
|`TIME_ZONE`    |Часовой пояс ([подробнее](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-TIME_ZONE))|Europe/Moscow|
|`DEBUG`        |Debug mode Django ([подробнее](https://docs.djangoproject.com/en/3.1/ref/settings/#debug))|True|

Python3 должен быть уже установлен.

Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

После установки запустите проект
```
python3 manage.py runserver 0.0.0.0:8000
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).