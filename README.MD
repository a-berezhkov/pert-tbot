# Создание телеграмм бота

Демо бота @petrspb_bot

1. Найдите в telegram @botfather  и пройдите авторизацию 
2. Введите команду ```/newbot``` (выберите имя бота и username | username - уникальный логи, оканчивающийся на _bot)
3. Запустите команду ```pip install python-telegram-bot``` ( документация на [GitHub](https://github.com/python-telegram-bot/python-telegram-bot) )
5. Полученный ключ от @botfather введите в переменную  ```BOT_KEY = "Ваш ключ" ```
4. При необходимости сформируйте меню в @botfather 
5. Запустите команду ```pip install requests`` \[только для примера\]
6. Для получения данных с сайтов можно использовать API: https://habr.com/ru/company/macloud/blog/562700/

# Публикация бота на Heroku (ветка heroku)

1. Полная интрукция [тут](https://towardsdatascience.com/how-to-deploy-a-telegram-bot-using-heroku-for-free-9436f89575d2)
2. Пройти регистрацию на [heroku.com](https://heroku.com/apps)
3. Создать новый проект и установить [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
4. Создать Procfile (см. пример в корне проекта)
5. Создать файл ```requirements.txt``` выполнив команду в консоли ```python pip freeze > requirements.txt ```
6. Так же необходимо внести изменения в файл ```bot.py```:

Заменить 

```python
updater.start_polling()
```
На

```python
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=BOT_KEY,
                          webhook_url="адрес приложения с Heroku" + BOT_KEY)
    updater.idle()
```

И добавить следующий код в начало проекта:

```python
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', 80))
```

7. Добавлена файлов в репозиторий для heroku (Ваш проект -> Вкладка "Deploy")

Все команды выполняются из корня проекта
```cmd
$ heroku login

$ git add .
$ git commit -am "make it better"
$ git push heroku master

```

Используйте ```  heroku logs --tail   ``` для просмотра логов и ошибок

