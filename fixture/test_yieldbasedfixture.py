import pytest 

@pytest.fixture
def yieldbasedfixure():
	print("printing before yield statement")
	yield
	print("printing after yield statement")


def test_yieldbasedfixture(yieldbasedfixure):
	print("yield based fixture")
