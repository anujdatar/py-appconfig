# AppConfig

Persistent configuration storage for python applications. Based on similar `npm` modules,
because of the lack of a `python` package that does something similar.

> **Note**: This package is still under development. Core functions work just fine,
> and as intended. But a few QOL features need to be worked in.

### Installation

```sh
# still in testing, pip package coming soon
pip install appconfig

# for now, package is active and working on TestPyPI
pip install -i https://test.pypi.org/simple/ appconfig
```

### Usage

```py
from appconfig import AppConfig

config = AppConfig(project_name="myProject")
config_values = {
    'number': 1234,
    'string': 'some random string'
}

for item in config_values:
    config.set(item, config_values[item])
    
print(config.get_all())
print(config.get('number'))
print(config.get('string'))
```

### Option/args during init

1. `project_name` : `str` -> **required**
2. `conf_name`: str -> *optional*, default = `config` (filename of config file)
3. `conf_ext`: str -> *optional*, default = `.json` (file extension for config file)
4. `verbose`: bool -> *optional*, default = `False` (for verbose logging, needs more work)

### Module functions

```py
from appconfig import AppConfig
config = AppConfig(project_name="myProject")

config.set(key: str, value: Any) -> None
config.get(key: str) -> Any
config.get_all() -> dict
```

### To-do

1. Implement a setting default values at init.
2. Delete/Reset individual config values.
3. Atomically writing configs to prevent corruptions due to runtime errors or system crashes.
4. A better validation system for config values. Right now it only makes sure it does not try to store a function.
5. Type annotations.


## Related

Loosely based on the same basic concept as some `npm` packages commonly used with javascript applications.
- [`conf`](https://github.com/sindresorhus/conf) and [`appconfig`](https://raw.githubusercontent.com/anujdatar/appconfig).

## License

[MIT](https://github.com/anujdatar/py-appconfig/blob/master/LICENSE) Copyright (c) 2019-2021 Anuj Datar
