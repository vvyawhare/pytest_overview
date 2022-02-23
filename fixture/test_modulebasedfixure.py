import pytest 
@pytest.fixture
def modulebasedfixture(scope="module"):
	print("module based fixture")
	test={"name":"fixture"}
	return test

def test_modulebasedfixute(modulebasedfixture):
	print("running module based fixture")
	print(modulebasedfixture)
