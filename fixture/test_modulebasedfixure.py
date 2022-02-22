import pytest 
@pytest.fixture
def modulebasedfixture(scope="module"):
	print("module based fixture")


def test_modulebasedfixute():
	print("running module based fixture")
