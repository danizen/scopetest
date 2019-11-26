import pytest
import random


@pytest.fixture(scope='class')
def thingy_byclass():
    return random.random()


@pytest.fixture(scope='function')
def thingy():
    return random.random()


@pytest.fixture(params=['firefox', 'chrome', 'phantomjs'])
def browser_name(request):
    return request.param


class Browser():
    def __init__(self, name):
        self.name = name


@pytest.fixture
def browser(browser_name):
    return Browser(browser_name)

