# slaves-bot-vk

[Бот для мини-игры ВКонтакте "Рабы"](https://vk.com/app7794757) 

[Тема на Lolzteam](https://lolz.guru/threads/2389937/)

[Группа ВКонтакте](https://vk.com/club203610366) с чатами, для помощи новичкам

## Какие настройки присутствуют? Настройка в Config.json
![image](https://i.imgur.com/SWIq9ZQ.png)
- Authorization. Авторизация
- Windows_title, true/false. Информация реального времени в титл консоли
- Telegram_notifications, true/false. Уведомления в телеграм
- Telegram_user_id. ID аккаунт телеграм
- Telegram_bot_token. Токен бота телеграм, получить здесь -> @BotFather
- Min/Max_delay. Рандомизация времени на выдачу цепей, покупку рабов и выдачу названвания работы
- Job_name. Имя, имена работ
- Min/Max_price. Минимальная и максимальная цена за которую покупать рабов
- Buy_slave, true/false. Покупка рабов
- Buy_fetter, true/false. Покупка оков

## Флуд в консоль ошибками
- Error when buying slave, possibly a cooldown. Возможно флуд-контроль на покупку рабов
- Error when installing the job, possibly cooldown. Возможно флуд-контроль на установку названия работы
- Error when buying fetter, possibly a cooldown. Возможно флуд-контроль на покупку оков
![image](https://i.imgur.com/E0GDfzN.png)

## Как не получить Cooldown (система антифлуда)
- Min_delay в Config.json не должен быть меньше 5 секунд
- Старайте указывать больше работ в Config.json (Job_name)

## Как обойти Cooldown?
Есть не точная информация, но она была проверена на нескольких людях
- Воспользуйтесь VPN, если айпи не статический - перезагрузите роутер. Сделайте, что угодно, но вы должны изменить свой IP на другой

## Запуск скрипта на Windows
- Скачать архив с репозитория
- Установить Python последней версии http://python.org
- Поставить галочку ADD TO PATH
- Установить модули pip install -r requirements.txt
- Запустить скрипт
- Ввести ключ:
![image](https://i.imgur.com/mZODDE7.png)

## Установка на Android
- Устанавливаем Termux с Play Market
- Запускаем Termux
- Пишем pkg install -y git
- Далее git clone https://github.com/vuchaev2015/slaves-bot-vk
- cd slaves-bot-vk
- sh fast-setup.sh
- Настраиваем конфиг. Nano config.json
![image](https://i.imgur.com/AnX1Cif.png)
- Ключ получить можно по инструкции ниже
- sh run.sh

## Как получить ключ?
- Заходим в приложение ["Рабы"](https://vk.com/app7794757)
- Открываем консоль CTRL + SHIFT + I
- Переходим по вкладку NETWORK
- В графе filter пишем start
- Обновляем страницу
- Копируем все из поля authorization
![image](https://i.imgur.com/0WT8GH1.png)

На Android можно получить ключ с помощью приложения F12 - Inspect Element
- https://play.google.com/store/apps/details?id=com.asfmapps.f12

## Планы на будущее
- <del>Добавить рандомизацию при установке работ</del> Добавлено!
- <del>Добавить более удобную и автоматизированную установку на Termux</del> Добавлено!

## Информация о последних обновлениях
- Добавлена рандомизация айди и покупка этих рабов, теперь они не генерируются с топа. (By Yagus228)
- Добавлена авторизация через конфиг
- Исправлена проблема с кодировкой (крашило скрипт при запуске)
- Добавлена покупка невидимых рабов в конфиге, по дефолту выключено
- Добавлена информация в реальном времени в титл консоли (Линуксоидам и термуксоидам - windows title поставить на false или будет флудить в консоль ошибкой :) )
- Удалили невидимых рабов , т.к они были пофикшены
- Добавлены уведомления Telegram
