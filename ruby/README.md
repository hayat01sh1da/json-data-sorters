## 1. Environment

- Ruby 4.0.2

## 2. Install Gems via Gemfile and Bundler

```command
$ bundle install
$ bundle lock --add-checksums
```

## 3. Execution

```command
$ cd ./ruby
$ ruby main.rb
Provide the directory name you put the JSON file in:
../json
Provide the filename of which JSON data name you would like to sort:
settings.json
Provide asc(default) or desc you would like to sort key-value in:
asc
Start exporting JSON data in ./json/settings.json
Done export JSON data in ./json/settings.json 🎉
```

## 4. Unit Test

```command
$ ruby test/application_test.rb 
Run options: --seed 44849

# Running:

.....

Finished in 0.106035s, 47.1541 runs/s, 75.4466 assertions/s.

5 runs, 8 assertions, 0 failures, 0 errors, 0 skips
```

## 5. Static Code Analysis

```command
$ rubocop
Inspecting 6 files
......

6 files inspected, no offenses detected
```

## 6. Type Checks

```command
$ rbs-inline --output sig/generated/ .
🎉 Generated 4 RBS files under sig/generated
$ steep check
# Type checking files:

........

No type error detected. 🧉
```
