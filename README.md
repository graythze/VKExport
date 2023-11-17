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
* Маркета (магазина) <kbd>[market.get](https://vk.com/dev/market.get)</kbd>
* Постов на стене <kbd>[wall.get](https://vk.com/dev/wall.get)</kbd>
* Сообщений <kbd>[messages.getById](https://vk.com/dev/messages.getById)</kbd>
* Комментарии под фото </kbd>[photos.getAllComments](https://vk.com/dev/photos.getAllComments)</kbd>

## ⚙️ Использование
1) Скачайте скрипт
2) Установите пакеты, используя команду `pip install -r requirements.txt`
3) Запустите скрипт, используя команду `python collector.py VK_TOKEN durov -api 5.82 -c wall,photos,notes -sf -v `

Команда `python collector.py -h` показана ниже

```
usage: collector.py [-h] [-c CUSTOM | -b | -e | -f] [-a API] [-sf] [-v]
                    token id

usage: collector.py VK_TOKEN durov -api 5.82 -c wall,photos,notes -sf -v       

positional arguments:
  token                 VK API token
  id                    Page ID or user domain

options:
  -h, --help            show this help message and exit
  -c CUSTOM, --custom CUSTOM
                        Parse custom methods
  -b, --base            Parse basic info
  -e, --extra           Parse basic + extra info
  -f, --full            Parse full info
  -a API, --api API     API version
  -sf, --singlefile     Save result in single file
  -v, --verbose         Increase output verbosity
```

### 📍 Аргументы
`token` - Токен VK API

`id` — идентификатор или домен страницы (например, `1`, `id1` или `durov`)

`-a, --apiver` — версия API VK, например `5.82`. Default: `5.82`

`-sf, --singlefile` - Сохранение результата в одном файле. По умолчанию, каждый метод сохраняется в отдельный файл

`-b, --base` — Базовый уровень парсера. Парсинг всех методов, кроме <kbd>[messages.getById](https://vk.com/dev/messages.getById)</kbd> и <kbd>[users.getFollowers](https://vk.com/dev/users.getFollowers)</kbd>

`-e, --extra ` — Средний уровень парсера. Парсинг всех методов, кроме <kbd>[messages.getById](https://vk.com/dev/messages.getById)</kbd> 

`-f, --full` — Полный уровень парсера. Парсинг всех представленных методов

`-v, --verbose` — Показать подробности

`-c, --custom` — Выбрать собственные методы. Например, при `photos,wall` будет использован парсинг только <kbd>[photos.get](https://vk.com/dev/photos.get)</kbd> и <kbd>[wall.get](https://vk.com/dev/wall.get)</kbd>

## 🔌 Получение API токена

### ⚡ Использование готовых решений
Сервис [*vkhost.github.io*](https://vkhost.github.io/) позволяет в автоматическом режиме собрать URL и получить токен
1) Откройте [*vkhost.github.io*](https://vkhost.github.io/)
2) Выберите приложение. Например, можно выбрать Kate Mobile или VFeed 
3) Нажмите на выбранное приложение
4) Нажмите на  "Продолжить как" или "Разрешить"
5) Скопируйте часть URL начиная с `access_token= ` и заканчивая `&expires_in`
6) Вставьте токен в скрипт

Также можно использовать другие приложения или службы для получения токена.

<h3 align="center">
  <b>⚠️⚠️⚠️</b>
</h3>

После использования скрипта, **в целях безпопасности КРАЙНЕ рекомендуется удалить API токен**. Это можно сделать двумя способами: [отозвать права на используемое приложения для токена](https://vk.com/settings?act=apps), либо [сменить пароль](https://id.vk.com/account/#/security)

### 💪 Собственная сборка URL
Получить ключ доступа пользователя можно одним из этих способов:

- [*Implicit Flow*](https://dev.vk.com/ru/api/access-token/implicit-flow-user): для работы с API от имени пользователя в Javascript-приложениях и Standalone-клиентах (десктопных или мобильных).

- [*Authorization Code Flow*](https://dev.vk.com/ru/api/access-token/authcode-flow-user): для работы с API от имени пользователя с серверной стороны вашего сайта.

Дополнительную информацию можно найти в [*Общих сведениях*](https://dev.vk.com/ru/api/access-token/getting-started)

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
1) Download script
2) Install packages using `pip install -r requirements.txt`
3) Run script using `python collector.py VK_TOKEN durov -api 5.82 -c wall,photos,notes -sf -v `

The command `python collector.py -h` is shown below
```
usage: collector.py [-h] [-c CUSTOM | -b | -e | -f] [-a API] [-sf] [-v]
                    token id

usage: collector.py VK_TOKEN durov -api 5.82 -c wall,photos,notes -sf -v       

positional arguments:
  token                 VK API token
  id                    Page ID or user domain

options:
  -h, --help            show this help message and exit
  -c CUSTOM, --custom CUSTOM
                        Parse custom methods
  -b, --base            Parse basic info
  -e, --extra           Parse basic + extra info
  -f, --full            Parse full info
  -a API, --api API     API version
  -sf, --singlefile     Save result in single file
  -v, --verbose         Increase output verbosity
```

### 📍 Arguments
`token` - VK API Token

`id` - ID or Page domain (e.g. `1`, `id1` or `durov`)

`api APIVER, --apiver APIVER` - VK API Version, eg `5.82`

`-sf, --singlefile ` - Save result in single file. Each file for method by default.

`-m [{1,2,3}], --mode [{1,2,3}]` - Parser complexity. `1` parses all except messages and followers, `2` parses all except messages, `3` parses all methods

`-b, --base` — Base parser complexity, instead <kbd>[messages.getById](https://vk.com/dev/messages.getById)</kbd> and <kbd>[users.getFollowers](https://vk.com/dev/users.getFollowers)</kbd>

`-e, --extra ` —  Extra parser complexity, instead <kbd>[messages.getById](https://vk.com/dev/messages.getById)</kbd> 

`-f, --full` — Full parser complexity. Parsing all methods

`-v, --verbose` — Показать подробности

`-v, --verbose` - Increase output verbosity

`-c, --custom` - Set custom methods, e.g. `photos,wall` will parse <kbd>[photos.get](https://vk.com/dev/photos.get)</kbd> and <kbd>[wall.get](https://vk.com/dev/wall.get)</kbd>

## 🔌 Getting VK API token

### ⚡ Third party services
Service [*vkhost.github.io*](https://vkhost.github.io/) helps automatically bulid URL and get token
1) Visit [vkhost.github.io](https://vkhost.github.io/)
2) Choose app. It's better to use token from Kate Mobile or VFeed apps 
3) Click on app 
4) Click on "Continue as" or "Allow"
5) Copy part of URL from `access_token= `to `&expires_in`
6) Paste token to CLI

You can use other apps or services to get token.

<h3 align="center">
  <b>⚠️⚠️⚠️</b>
</h3>

After using the script **for security reasons, it is HIGHLY recommended to remove the API token**. It is possible to do in two ways: [*revoke app authorization which was used to obtain token*](https://vk.com/settings?act=apps), or [*change the password*](https://id.vk.com/account/#/security)

### 💪 Self-building URL

To get api token you can use one of them ways:

- [*Implicit Flow*](https://dev.vk.com/en/api/access-token/implicit-flow-user): to work with API on behalf of the user in Javascript applications and Standalone clients (desktop or mobile).

- [*Authorization Code Flow*](https://dev.vk.com/en/api/access-token/authcode-flow-user): to work with API on behalf of the user from the server side of your site.

You can find extra information at [*General information*](https://dev.vk.com/en/api/access-token/getting-started)

## NOTE: If result JSON file is too large, you can get MemoryError error. To avoid it, [install x64 Python version](https://www.python.org/downloads/)
