Небольшой сервис отправки имейл рассылок на Python, Django. 
Используйтся Python 2.7.18.

**Возможности сервиса:**

1. Отправка рассылок с использованием html макета и списка подписчиков.
2. Для создания рассылки использовать ajax запрос. Форма для создания рассылки заполняется в модальном окне. Использовать библиотеки: jquery, bootstrap.
3. Отправка отложенных рассылок.
4. Использование переменных в макете рассылки. (Пример: имя, фамилия, день рождения из списка подписчиков)
5. Отслеживание открытий писем.
6. Отложенные отправки реализованы при помощи Celery.

**Дополнительно:**

В этом проекте рассылки представляют собой email-сообщение, которое будет запланировано на доставку заданному множеству подписчиков.
Доставка этого email-сообщения произойдёт через 30-32 дней с момента его отправки оператором. Предположим, что именно такой срок предполагается,
если не возникнет сбой на сервере.

Образец сообщения определён в шаблоне `./src/static_dev/assets/email_message.html`.

Сборка `./docker-compose.yaml` преднаначена для развёртывания в разработке на локальном сервере, чтобы просто ознакомиться с проектом.

!NB Для рассылки сервис позволяет выбирать любых подписчиков, для которых:

 - email уже был отправлен, при этом время с момента отправки задания на рассылку составляет 30 и более дней (настраивается `app_settings.DAYS_UNTIL_EMAIL_SENT`),
 - если с момента просмотра* письма подписчиком прошло 104 недели (два года) или больше (настраивается `app_settings.TIMES_SINCE_EMAIL_SEEN`).


\* Просмотр письма подписчиком не гарантирован, так как почтовые сервисы могут отправить письмо в спам.
При попадании письма в спам, атрибут ссылки изображения может быть удалён (Google). Некоторые сервисы и вовсе 
загружают изображение на свои сервера, меняя ссылку (Mail.ru).

**Настройки проекта:**

- Переменные среды: `./src/.env`

    Здесь необходимо определить:

        - `BASE_URL` - базовый адрес лок. сервера - в соответствии с запуском проекта (номер порта определён в скрипте `./server-entrypoint.sh`),

        - `EMAIL_HOST_USER` - email почтового сервиса откуда идут рассылки,
        - `EMAIL_HOST_PASSWORD` - пароль,
        - `TZ` - часовой пояс

        Параметры суперпользователя:

            - `DJANGO_SUPERUSER_USERNAME`,
            - `DJANGO_SUPERUSER_PASSWORD`,
            - `DJANGO_SUPERUSER_EMAIL`

- Точки входа (sh-скрипты): 

    - Точка входа в django процесс: `./server-entrypoint.sh`:

        1. Параметры для команды создания суперпользователя `createsuperuser_from_settings` определены в файле .env.

        2. Если не собираетесь создавать своих пользователей (подписчиков) в консоли или в админ-панели, то раскоментируйте последние строки и поменяйте параметры: 
        username, password, email, first_name, last_name.

    - Точка входа для worker: `./worker-entrypoint.sh`
    

Запуск проекта:

```
docker-compose up -d --build
docker-compose up
```