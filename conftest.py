import pytest

CONFIG = None


def pytest_addoption(parser):
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
    import os
    import json
    import utilities

    project_path = os.path.dirname(utilities.__file__)
    environment = dict(PROD=os.path.join(project_path, 'config.prod.json'))

    config_file_path = environment[request.config.getoption('--environment').upper()]
    with open(config_file_path) as config_file:
        global CONFIG
        CONFIG = json.load(config_file)
    CONFIG['BROWSER'] = request.config.getoption('--browser-name')
    print(f"{CONFIG}")


@pytest.fixture()
def try_new(request):
    print('1232131')
