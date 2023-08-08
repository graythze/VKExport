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
usage: collector.py [-h] [-api APIVER] [-s [{1,2}]] [-m [{1,2,3}]]      
                    [-v [{1,2}]]                                        
                    token id                                            
                
Use example: python collector.py <API token> <page id> -v <API ver> -s  
<save option>

positional arguments:
  token                 VK API token
  id                    Page ID or custom user domain

options:
  -h, --help            show this help message and exit
  -api APIVER, --apiver APIVER
                        Enter API version
  -s [{1,2}], --save [{1,2}]
                        Save method
  -m [{1,2,3}], --mode [{1,2,3}]
                        Parser complexity.
  -v [{1,2}], --verbose [{1,2}]
                        Set verbose level for CLI
```
### 📍 Arguments
`token` - VK API Token

`id` - ID or Page domain (eg. `1`, `id1` or `durov`)

`api APIVER, --apiver APIVER` - VK API Version

`-s [{1,2}], --save [{1,2}]` - Save method. `1` saves every method separately, `2` saves in one file

`-m [{1,2,3}], --mode [{1,2,3}]` - Parser complexity. `1` parses all except messages and followers, `2` parses all except messages, `3` parses all methods,

`-v [{1,2}], --verbose [{1,2}]` - Set verbose level for CLI. `1` prints successful requests, `2` prints raw JSON requests

## 🔌 Run script
* Get VK API token and ID or domain of user
* Run script using 
  
    `py collector.py <API token> <page id> -v <API ver> -s <save method> -m <parser mode> -v <verbose level>` to parse data in one file

*You can set custom API version adding `-a <API version>`*

*To set single file instead of using separate ones, use  `-s sin`*

## NOTE: If your JSON file is too large, you can get MemoryError error. To avoid it, [install x64 Python version](https://stackoverflow.com/a/37726090)
