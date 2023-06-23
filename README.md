# 📄 VKExport

VKExport allows you export data in JSON file from your or friend's VK page

## ✅ Export available for
* Main profile data
* Documents  data
* Friends data
* Gifts data
* Notes data
* Photos data
* Stories data
* Videos data
* Page followers data
* Groups data
* Market data
* Wall data

## Usage
Run `python collector.py -h`

```
usage: collector.py [-h] [-v VER] [-s SAVE] token page

Use example: python collector.py <API token> <page id> -v <API ver> -s <save        
option>

positional arguments:
  token                 VK API token
  page                  Page ID or custom user domain

options:
  -h, --help            show this help message and exit
  -v VER, --ver VER     Enter API version (5.82 is set by default)
  -s SAVE, --save SAVE  Save as single file or file separated by method (separate   
                        file is used by default)
```

## 🔌 Run script
* Get VK API token and ID or domain of user
* Run script using 
  
    `python collector.py <API token> <page id> -v <API ver> -s <save option>` to parse data in one file

*You can set custom API version adding `-a <API version>`*

*To set single file instead of using separate ones, use  `-s sin`*

## NOTE: If your JSON file is too large, you can get MemoryError error. To avoid it, [install x64 Python version](https://stackoverflow.com/a/37726090)
