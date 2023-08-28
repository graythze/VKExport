<h1 align="center">
  VKExport 📄

  [RUS](#-что-это) // [ENG](#-what-is-it)
</h1>

<h1 align="center">
  <a href="#rus"><b>RUS</b></a>
</h1>

# 📄 Что это?

VKExport позволяет экспортировать данные в файл JSON с личной страницы ВК или другого человека.

## ✅ Экспорт доступен для
* Данных профиля <kbd>[users.get](https://vk.com/dev/users.get)</kbd>
* Документов <kbd>[docs.get](https://vk.com/dev/docs.get)</kbd>
* Друзей <kbd>[friends.get](https://vk.com/dev/friends.get)</kbd>
* Подарков <kbd>[gifts.get](https://vk.com/dev/gifts.get)</kbd>
* Заметок <kbd>[notes.get](https://vk.com/dev/notes.get)</kbd>
* Фотографий <kbd>[photos.get](https://vk.com/dev/photos.get)</kbd>
* Историй <kbd>[stories.get](https://vk.com/dev/stories.get)</kbd>
* Видео <kbd>[video.get](https://vk.com/dev/video.get)</kbd>
* Подписчиков <kbd>[users.getFollowers](https://vk.com/dev/users.getFollowers)</kbd>
* Групп и публичных страниц <kbd>[groups.get](https://vk.com/dev/groups.get)</kbd>
* Маркета <kbd>[market.get](https://vk.com/dev/market.get)</kbd>
* Постов на стене <kbd>[wall.get](https://vk.com/dev/wall.get)</kbd>
* Сообщений <kbd>[messages.getById](https://vk.com/dev/messages.getById)</kbd>

## ⚙️ Использование
* Пример запуска

  `py collector.py <API token> <page id> -v <API ver> -s <save method> -m <parser mode> -v`

Команда `py collector.py -h` показана ниже

```
usage: collector.py [-h] [-c CUSTOM | -m {1,2,3}] [-api APIVER] [-sf]
                    [-v]
                    token id

Use example: py collector.py <API token> <page id> -v <API ver> -s      
<save method> -m <parser mode> -v

positional arguments:
  token                 VK API token
  id                    Page ID or user domain

options:
  -h, --help            show this help message and exit
  -c CUSTOM, --custom CUSTOM
                        Choose custom methods
  -m {1,2,3}, --mode {1,2,3}
  -api APIVER, --apiver APIVER
                        API version
  -sf, --singlefile     Save result in single file
  -v, --verbose         Increase output verbosity
```

### 📍 Аргументы
`token` - Токен VK API

`id` — идентификатор или домен страницы (например, `1`, `id1` или `durov`)

`api APIVER, --apiver APIVER` — версия API VK, например `5.82`

`-sf, --singlefile ` - Сохранение результата в одном файле. По умолчанию, каждый метод сохраняется в отдельный файл

`-m [{1,2,3}], --mode [{1,2,3}]` — уровень парсера. `1` парсинг всех методов, кроме сообщений и подписчиков, `2` парсинг всех методов, кроме сообщений, `3` парсинг всех методов,

`-v, --verbose` — показать подробности

`-c, --custom` — Выбрать собственные методы. Например. `photos,wall` будет использован парсинг только фотографий и стены пользователя.

## 🔌 Получение API токена
1) Откройте [vkhost.github.io](https://vkhost.github.io/)
2) Выберите приложение. Лучше всего использовать приложения Kate Mobile или VFeed 
3) Нажмите на выбранное приложение
4) Нажмите на  "Продолжить как" или "Разрешить"
5) Скопируйте часть URL начиная с `access_token= ` и заканчивая `&expires_in`
6) Вставьте токен в скрипт

Также можно использовать другие приложения или службы для получения токена.

## ПРИМЕЧАНИЕ: Если JSON файл слишком большой, есть вероятность получить ошибку MemoryError. Чтобы исправить это, [установите x64 версию Python ](https://www.python.org/downloads/)

<h1 align="center">
  <a href="#eng"><b>ENG</b></a>
</h1>

## 📄 What is it?
VKExport allows you to export data in JSON file from personal or other VK pages

## Export available for
* Profile data <kbd>[users.get](https://vk.com/dev/users.get)</kbd>
* Documents <kbd>[docs.get](https://vk.com/dev/docs.get)</kbd>
* Friends <kbd>[friends.get](https://vk.com/dev/friends.get)</kbd>
* Gifts <kbd>[gifts.get](https://vk.com/dev/gifts.get)</kbd>
* Notes <kbd>[notes.get](https://vk.com/dev/notes.get)</kbd>
* Photos <kbd>[photos.get](https://vk.com/dev/photos.get)</kbd>
* Stories <kbd>[stories.get](https://vk.com/dev/stories.get)</kbd>
* Videos <kbd>[video.get](https://vk.com/dev/video.get)</kbd>
* Followers <kbd>[users.getFollowers](https://vk.com/dev/users.getFollowers)</kbd>
* Groups, public pages <kbd>[groups.get](https://vk.com/dev/groups.get)</kbd>
* Market items <kbd>[market.get](https://vk.com/dev/market.get)</kbd>
* Wall posts <kbd>[wall.get](https://vk.com/dev/wall.get)</kbd>
* Messages <kbd>[messages.getById](https://vk.com/dev/messages.getById)</kbd>

## ⚙️ Usage
* Use example:

  `py collector.py <API token> <page id> -v <API ver> -s <save method> -m <parser mode> -v`

The command `py collector.py -h` output is shown below

```
usage: collector.py [-h] [-c CUSTOM | -m {1,2,3}] [-api APIVER] [-sf]
                    [-v]
                    token id

Use example: py collector.py <API token> <page id> -v <API ver> -s      
<save method> -m <parser mode> -v

positional arguments:
  token                 VK API token
  id                    Page ID or user domain

options:
  -h, --help            show this help message and exit
  -c CUSTOM, --custom CUSTOM
                        Choose custom methods
  -m {1,2,3}, --mode {1,2,3}
  -api APIVER, --apiver APIVER
                        API version
  -sf, --singlefile     Save result in single file
  -v, --verbose         Increase output verbosity
```

### 📍 Arguments
`token` - VK API Token

`id` - ID or Page domain (e.g. `1`, `id1` or `durov`)

`api APIVER, --apiver APIVER` - VK API Version, eg `5.82`

`-sf, --singlefile ` - Save result in single file. Each file for method by default.

`-m [{1,2,3}], --mode [{1,2,3}]` - Parser complexity. `1` parses all except messages and followers, `2` parses all except messages, `3` parses all methods

`-v, --verbose` - Increase output verbosity

`-c, --custom` - Set custom methods, e.g. `photos,wall` will parse photos and wall data

## 🔌 Getting VK API token
1) Visit [vkhost.github.io](https://vkhost.github.io/)
2) Choose app. It's better to use token from Kate Mobile or VFeed apps 
3) Click on app 
4) Click on "Continue as" or "Allow"
5) Copy part of URL from `access_token= `to `&expires_in`
6) Paste token to CLI

You can use other apps or services to get token.

## NOTE: If result JSON file is too large, you can get MemoryError error. To avoid it, [install x64 Python version](https://www.python.org/downloads/)
