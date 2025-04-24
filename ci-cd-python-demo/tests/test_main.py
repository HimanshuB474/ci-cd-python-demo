# tests/test_main.py

from user_service.main import add

def test_add():
    assert add(2, 3) == 5

