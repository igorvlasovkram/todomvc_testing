import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def clear_storage():
    yield
    browser.clear_local_storage()
