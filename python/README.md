## 1. Environment

- Python 3.14.4

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

```command
$ python main.py
Provide the directory name you put the JSON file in: ../json
Provide the filename of which JSON data name you would like to sort: settings.json
Provide asc(default) or desc you would like to sort key-value in: asc
Start exporting JSON data in ./json/settings.json
Done exporting JSON data in ./json/settings.json 🎉
```

## 4. Unit Test

```command
$ pytest 
============================= test session starts ==============================
platform linux -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0
rootdir: /mnt/c/Users/binlh/Documents/development/json-data-sorters/python
collected 5 items

test/test_application.py .....                                           [100%]

============================== 5 passed in 0.26s ===============================
```
