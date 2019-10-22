import pytest

CONFIG = None


def pytest_addoption(parser):
    """
    Отримання аргументів браузера та середовища з консолі
    """
    parser.addoption('--browser-name',
                     dest='browser-name',
                     type=str,
                     default='chrome',
                     help='Browser name. Could be chrome, firefox')
    parser.addoption('--environment',
                     dest='environment',
                     type=str,
                     default='prod',
                     help='Environment on which run tests. Only prod available')


@pytest.fixture(scope='session', autouse=True)
def get_config(request):
    """
    Створення файлу конфігурації
    """
    import os
    import json
    import utilities

    # шлях до папки з утілітами
    project_path = os.path.dirname(utilities.__file__)
    # словник з ключем середовища
    environment = dict(PROD=os.path.join(project_path, 'config.json'))
    # вибір необхідної конфігурації середовища
    config_file_path = environment[request.config.getoption('--environment').upper()]
    # створення посилання на json файл конфігурації
    with open(config_file_path) as config_file:
        global CONFIG
        CONFIG = json.load(config_file)
    # запис до json файлу конфігурації типу браузера
    CONFIG['BROWSER'] = request.config.getoption('--browser-name')
