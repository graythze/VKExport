# 📄 VKExport

VKExport allows you export data in JSON file from your or friend's VK page

## ✅ Export available for
* Main profile data
* Documents  data
* Friends data
* Gifts data
* Notes data
* Photos data
* Stories data (if they are available)
* Videos data
* Page followers data
* Groups data
* Market data
* Wall data

## Usage
Run `python collector.py -h`

```
usage: collector.py [-h] [-t T] [-p P] [-a A] [-s S]

Use example: python collector.py <API token> <page id> -a <API ver> -s <save
option>

options:
  -h, --help      show this help message and exit
  -t T, -token T  VK API token
  -p P, -page P   Page ID or custom user's domain
  -a A, -api A    Enter API version (5.82 is set by default)
  -s S, -save S   Save as single file or file separated by method (separate file
                  is used by default)
```

## 🔌 Run script
* Get VK API token and ID or domain of user
* Run script using 
  
    `python collector.py <API token> <page id> -a <API ver> -s <save option>` to parse data in one file

*You can set custom API version adding `-a <API version>`*

*To set single file instead of using separate ones, use  `-s sin`*

## NOTE: If your JSON file is too large, you can get MemoryError error. To avoid it, [install x64 Python version](https://stackoverflow.com/a/37726090)
