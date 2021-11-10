from os.path import exists
import shutil
from appconfig import AppConfig

a = AppConfig(project_name='test', verbose=True)


def test_file_creation():
    filepath = a.config_path
    assert exists(filepath)


# write test configuration values to
test_config = {
    "number": 1234,
    "string": "some string value"
}
for item in test_config:
    a.set(item, test_config[item])
a.write_conf()


def test_get_all_function():
    assert a.get_all() == test_config


def test_individual_config_vales():
    assert a.get("number") == 1234
    assert a.get("string") == "some string value"


def test_do_cleanup():
    """Should probably set up test setup and teardown instead of this"""
    print('Performing cleanup')
    print('deleting test config dir')
    shutil.rmtree(a.config_folder)
    assert not exists(a.config_folder)
