# 📄 VKExport

VKExport allows you export data in JSON file from your or friend's VK page

## ✅ Export available for
* Main profile data ([users.get](https://vk.com/dev/users.get))
* Documents ([docs.get](https://vk.com/dev/docs.get))
* Friends ([friends.get](https://vk.com/dev/friends.get))
* Gifts ([gifts.get](https://vk.com/dev/gifts.get))
* Notes ([notes.get](https://vk.com/dev/notes.get))
* Photos ([photos.get](https://vk.com/dev/photos.get))
* Stories ([stories.get](https://vk.com/dev/stories.get))
* Videos ([video.get](https://vk.com/dev/video.get))
* Followers ([users.getFollowers](https://vk.com/dev/users.getFollowers))
* Groups and public pages ([groups.get](https://vk.com/dev/groups.get))
* Market items ([market.get](https://vk.com/dev/market.get))
* Wall posts ([wall.get](https://vk.com/dev/wall.get))
* Messages ([messages.getById](https://vk.com/dev/messages.getById))

## ⚙️ Usage
Run `py collector.py -h`

```
usage: collector.py [-h] [-c CUSTOM | -m {1,2,3}] [-api APIVER] [-sf]
                    [-v]
                    token id

Use example: py collector.py <API token> <page id> -v <API ver> -s      
<save method> -m <parser mode> -v <verbose level>

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

`id` - ID or Page domain (eg. `1`, `id1` or `durov`)

`api APIVER, --apiver APIVER` - VK API Version, eg `5.82`

`-sf, --singlefile ` - Save result in single file. Each file for method by default.

`-m [{1,2,3}], --mode [{1,2,3}]` - Parser complexity. `1` parses all except messages and followers, `2` parses all except messages, `3` parses all methods,

`-v, --verbose` - Increase output verbosity

`-c, --custom` - Set custom methods, eg. `photos,wall` will parse photos and wall data

## 🔌 Run script
* Get VK API token and ID or domain of user
* Run script using 
  
    `py collector.py <token> <page_id> -api <api version> -m <parser mode> [-sf] [-v] [-c]`

## NOTE: If your JSON file is too large, you can get MemoryError error. To avoid it, [install x64 Python version](https://stackoverflow.com/a/37726090)

# 📄 VKExport

VKExport позволяет экспортировать данные в файл JSON со страницы ВК вашей компании или друга.

## ✅ Экспорт доступен для
* Основные данные профиля ([users.get](https://vk.com/dev/users.get))
* Документы ([docs.get](https://vk.com/dev/docs.get))
* Друзья ([friends.get](https://vk.com/dev/friends.get))
* Подарки ([gifts.get](https://vk.com/dev/gifts.get))
* Заметки ([notes.get](https://vk.com/dev/notes.get))
* Фотографии ([photos.get](https://vk.com/dev/photos.get))
* Истории ([stories.get](https://vk.com/dev/stories.get))
* Видео ([video.get](https://vk.com/dev/video.get))
* Подписчики ([users.getFollowers](https://vk.com/dev/users.getFollowers))
* Группы и паблики ([groups.get](https://vk.com/dev/groups.get))
* Предметы с рынка ([market.get](https://vk.com/dev/market.get))
* Сообщения на стене ([wall.get](https://vk.com/dev/wall.get))
* Сообщения ([messages.getById](https://vk.com/dev/messages.getById))

## ⚙️ Использование
Запустите `py Collector.py -h`

```
использование: Collector.py [-h] [-c ПОЛЬЗОВАТЕЛЬСКИЙ | -m {1,2,3}] [-api APIVER] [-sf]
                     [-в]
                     идентификатор токена

Пример использования: py Collector.py <токен API> <идентификатор страницы> -v <версия API> -s
<метод сохранения> -m <режим анализатора> -v <уровень подробного описания>

позиционные аргументы:
   токен API токен ВК
   id Идентификатор страницы или домен пользователя

параметры:
   -h, --help показать это справочное сообщение и выйти
   -c ПОЛЬЗОВАТЕЛЬСКИЙ, --custom ПОЛЬЗОВАТЕЛЬСКИЙ
                         Выбирайте собственные методы
   -m {1,2,3}, --mode {1,2,3}
   -api APIVER, --apiver APIVER
                         версия API
   -sf, --singlefile Сохранить результат в один файл
   -v, --verbose Увеличить детализацию вывода
```
### 📍 Аргументы
`token` - Токен API ВК

`id` — идентификатор или домен страницы (например, `1`, `id1` или `durov`)

`api APIVER, --apiver APIVER` — версия API ВК, например `5.82`

`-sf, --singlefile ` - Сохранить результат в одном файле. Каждый файл для метода по умолчанию.

`-m [{1,2,3}], --mode [{1,2,3}]` — сложность парсера. `1` анализирует все, кроме сообщений и подписчиков, `2` анализирует все, кроме сообщений, `3` анализирует все методы,

`-v, --verbose` — увеличить детализацию вывода

`-c, --custom` — Установить собственные методы, например. `photos,wall` будет анализировать фотографии и данные стен.

## 🔌 Запустить скрипт
* Получите токен VK API и идентификатор или домен пользователя.
* Запустите скрипт, используя
  
     `py Collector.py <токен> <page_id> -api <версия API> -m <режим анализатора> [-sf] [-v] [-c]`

## ПРИМЕЧАНИЕ. Если ваш файл JSON слишком велик, вы можете получить ошибку MemoryError. Чтобы этого избежать, [установите версию Python x64] (https://stackoverflow.com/a/37726090)