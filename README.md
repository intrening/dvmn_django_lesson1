# Сайт-аналог Яндекс.Афиши для Артема

Учебный сайт-аналог сервиса Яндекс.Афиша. Позволяет добавлять на карту объекты с текстовым описанием и фотографиями.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

В каталоге с программой создайте файл .env, в котором укажите переменные:

`DJANGO_SECRET_KEY` - секретный ключ Django

`DJANGO_DEBUG` - True, если девелоперская версия сайта и False, если продакшн-версия

Запуск девелоперской версии сайта:
```
python manage.py runserver
```


### Пример использования
Загруженный и работающий сайт: [https://wol87.pythonanywhere.com/](https://wol87.pythonanywhere.com/)
Админка сайта:  [https://wol87.pythonanywhere.com/admin/](https://wol87.pythonanywhere.com/admin/)

Данные взяты с сайта [https://github.com/devmanorg/where-to-go-places](https://github.com/devmanorg/where-to-go-places)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).