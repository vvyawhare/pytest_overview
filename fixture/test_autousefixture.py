import pytest


@pytest.fixture(autouse=True)
def function_autouse():
    print("scope function with autouse")
    
def test_autouse():
    assert True
