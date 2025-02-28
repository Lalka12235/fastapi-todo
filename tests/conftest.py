import pytest

#data for test
@pytest.fixture
def test_task_for_create():
    return {
        'title': 'test',
        'description': 'make test on pytest',
        'check': False,
    }

@pytest.fixture
def test_task_for_update():
    return{
        'title': 'test',
        'description': 'make test on pytest',
        'check': True,
    }