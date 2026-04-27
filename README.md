# SSH Botnet
[![Python3.x](https://img.shields.io/badge/python-3.x-FADA5E.svg?logo=python)](https://www.python.org/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-red.svg)](https://www.python.org/dev/peps/pep-0008/)

This script can send command to a list of ssh server written in python3.

You need to add bot in the script by yourself.

## Usage
```
    python3 ssh_botnet.py
```
**_Add bot:_**
``` 
    Line 48:
        add_client('host', 'username', 'password')
```

**Sometimes it will occur some bugs like:**
```
   AttributeError: 'NoneType' object has no attribute 'sendline'
```
