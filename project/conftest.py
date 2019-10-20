import pytest
from utilities import settings


def pytest_addoption(parser):
    parser.addoption('--browser-name',
                     dest='browser-name',
                     type=str,
                     default='chrome',
                     help='Browser name. Could be chrome, firefox')
    parser.addoption('--environment',
                     dest='environment',
                     type=str,
                     default='dev',
                     help='Environment on which run tests. Only prod available')


@pytest.fixture(scope='session', autouse=True)
def get_browser_name(request):
    settings.browser_name = request.config.getoption('--browser-name')


@pytest.fixture(scope='session', autouse=True)
def get_base_url(request):
    get_environment(request)
    if 'prod' in settings.environment:
        settings.host = 'google.com'
    settings.base_url = 'https://' + settings.host


def get_environment(request):
    settings.environment = request.config.getoption('--environment')
