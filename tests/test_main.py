from os.path import exists
import shutil
from appconfig import AppConfig

_defaults = {
    'a': 10,
    'b': 'this is a b'
}

_conf = {
    'projectName': 'test',
    'projectId': 'test',
    'version': '0.0.1',
    'a': 10,
    'b': 'this is a b'
}

a = AppConfig(project_name='test', verbose=True, defaults=_defaults)


def test_file_creation():
    filepath = a.config_path
    assert exists(filepath)


def test_get():
    assert a.get('projectName') == 'test'
    assert a.get('projectId') == 'test'
    assert a.get('version') == '0.0.1'


def test_get_all_function():
    assert a.get_all() == _conf


def test_defaults():
    assert a.get('a') == 10
    assert a.get('b') == 'this is a b'


def test_set():
    a.set('a', 1000)
    assert a.get('a') == 1000


def test_reset():
    a.reset('a')
    assert a.get('a') == 10


def test_set_new():
    _test_config = {
        'number': 1234,
        'string': 'some string value'
    }
    for (key, value) in _test_config.items():
        a.set(key, value)

    assert a.get('number') == 1234
    assert a.get('string') == 'some string value'


def test_reset_all():
    a.reset_all()
    assert a.get_all() == _conf


def test_delete():
    del _conf['b']
    a.delete('b')
    assert a.get_all() == _conf


def test_do_cleanup():
    """Should probably set up test setup and teardown instead of this"""
    print('Performing cleanup')
    print('deleting test config dir')
    shutil.rmtree(a.config_folder)
    assert not exists(a.config_folder)
