import pytest

@pytest.fixture
def sessionbasedfixture(scope="session"):
	print("session based fixture")

def test_sessionbased_fixture():
	print("running session based fixture")