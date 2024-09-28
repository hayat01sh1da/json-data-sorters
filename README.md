## 1. Common Environment

- WSL(Ubuntu 20.04.6 LTS)

## 2. READMEs

- [Ruby](./ruby/README.md)
- [Python](./python/README.md)

## 3. How to Use

In you terminal, provide the following 3 parameters via interactive user inputs.

- `dirname`: The directory name you put the JSON file in
- `filename`: The filename of which JSON data name you would like to sort
- `order`: `asc`(default) or `desc` you would like to sort key-value in

### 3-1. For Ruby Lovers

```command
$ cd ./ruby/
$ ruby main.rb 
Provide the directory name you put the JSON file in
../json
Provide the filename of which JSON data name you would like to sort
settings.json
Provide asc(default) or desc you would like to sort key-value in
asc
Start exporting JSON data in ./json/settings.json
Done export JSON data in ./json/settings.json 🎉
```

### 3-2. For Python Lovers

```command
$ cd ./python/
$ python main.py
Provide the directory name you put the JSON file in: ../json
Provide the filename of which JSON data name you would like to sort: settings.json
Provide asc(default) or desc you would like to sort key-value in: asc
Start exporting JSON data in ./json/settings.json
Done exporting JSON data in ./json/settings.json 🎉
```
