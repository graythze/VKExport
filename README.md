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
* **OWN messages**

## 🔌 Run script
* Get VK API token and ID or domain of user
* *If you want, you can set custom API version in `v` variable*
* Run script using 
  
    `python collector.py <API token> <page id>` to parse data in one file

    `python collector32.py <API token> <page id>` to parse data in separate files

## NOTE: If your JSON file is too large, you can get MemoryError error. To avoid it, install x64 Python version
