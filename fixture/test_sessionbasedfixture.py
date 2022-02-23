import pytest

@pytest.fixture
def sessionbasedfixture(scope="session"):
	print("session based fixture")
	test={"name":"divya"}
	return test


def test_sessionbased_fixture(sessionbasedfixture):
	print("running session based fixture")
	print(sessionbasedfixture)