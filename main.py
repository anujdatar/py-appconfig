from environ_paths import env_paths
from pathlib import Path
import json


def value_type_check(value):
    _acceptable = [str, int, float, complex, dict, list, tuple, bool, type(None)]
    if type(value) not in _acceptable:
        print('value is of type: ', type(value))
        raise ValueError


class AppConfig:
    """
    app config object for a python app
    :param:
        kwargs: project_name (String) -> mandatory
                conf_name (String) -> optional, default = config
                conf_ext (String) -> optional, default = .json
                verbose (Boolean) -> optional, default = False
    :return: persistent config file for project in default config location
    """

    def __init__(self, **kwargs):
        super().__init__()

        # get all kwargs passed to class constructor
        self.project_name = kwargs['project_name']
        self.conf_name = kwargs.get('conf_name', 'config')
        self.conf_ext = kwargs.get('conf_ext', '.json')
        self.verbose = kwargs.get('verbose', False)

        self.conf_file = self.conf_name + self.conf_ext
        self.config_folder = env_paths(self.project_name)['config']
        self.config_path = self.config_folder / self.conf_file
        self.temp_conf = self.config_folder / 'tmpfile'
        self.verbose_log('Config Path: ', self.config_path)

        # verify config folder and file exist, if not create
        Path.mkdir(self.config_folder, parents=True, exist_ok=True)
        Path.touch(self.config_path)

        self.validate()
        self.config = self.get_all()

    def validate(self):
        """verify if config file is valid json"""
        with open(self.config_path, 'r') as f:
            _data = f.read()
        try:
            _config = json.loads(_data)
            self.verbose_log('Config file exists and is valid JSON')
        except json.JSONDecodeError:
            self.verbose_log('Invalid config file, replacing with empty JSON')
            with open(self.config_path, 'w') as f:
                json.dump({}, f)

    def get_all(self):
        """get all values stored in config file"""
        with open(self.config_path) as f:
            return json.load(f)

    def get(self, key):
        """get single config value from config store"""
        try:
            return self.config[key]
        except KeyError:
            self.verbose_log('Invalid key')
            return

    def set(self, key, value):
        """set value of configuration in store"""
        # validate key data type
        if type(key) != str:
            raise KeyError
        # validate value data type
        value_type_check(value)
        try:
            self.config[key] = value
        except json.JSONEncoder:
            print('aaaaaaa')

        # write config to file
        self.write_conf()

    def verbose_log(self, *args):
        """print statements if you want a verbose run for debug"""
        if self.verbose:
            print(*args)

    def write_conf(self):
        # TODO make writing file atomic
        # check 'http://stupidpythonideas.blogspot.com/2014/07/getting-atomic-writes-right.html'
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f)


# test module functionality
if __name__ == '__main__':
    a = AppConfig(project_name='test', verbose=True)
    test = {
        "test": 1234,
        "something": "else"
    }
    for item in test:
        a.set(item, test[item])
    a.write_conf()

    with open(a.config_path) as f:
        __data = json.load(f)

    try:
        assert __data["test"] == 1234
        assert __data["something"] == "else"
        print('Tests passed')
    except AssertionError:
        print('Test failed, proper data write failure')

    print('deleting test config dir')
    import shutil
    shutil.rmtree(a.config_folder)
