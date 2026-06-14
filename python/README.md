## 1. Environment

- Python 3.14.6

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

```command
$ invoke run_json_data_sorter
Provide the directory name you put the JSON file in
../json
Provide the filename of which JSON data name you would like to sort
settings.json
Provide asc(default) or desc you would like to sort key-value in
asc
Start exporting JSON data in ./json/settings.json
Done exporting JSON data in ./json/settings.json 🎉
```

## 4. Unit Test

```command
$ invoke
============================= test session starts ==============================
platform linux -- Python 3.14.6, pytest-9.0.3, pluggy-1.6.0
rootdir: json-data-sorters/python
configfile: pyproject.toml
collected 5 items

test/test_application.py .....                                           [100%]

============================== 5 passed in 0.39s ===============================
```

## 5. Static Code Analysis

```command
$ flake8 .
./src/application.py:59:80: E501 line too long (80 > 79 characters)
./src/application.py:76:80: E501 line too long (82 > 79 characters)
./test/test_application.py:132:80: E501 line too long (85 > 79 characters)
./test/test_application.py:139:80: E501 line too long (96 > 79 characters)
./test/test_application.py:146:80: E501 line too long (84 > 79 characters)
$ autoflake8 --in-place --remove-duplicate-keys --remove-unused-variables --recursive .
$ autopep8 --in-place --aggressive --aggressive --recursive .
```

## 6. Type Checks

```command
$ mypy .
Success: no issues found in 4 source files
```
