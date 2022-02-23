import pytest

@pytest.fixture(scope="session")
def samplefixure():
	print("sample fixture")
	test={"name":"fixture"}
	return test
	#reading file

def test_samplefixture(samplefixure):
	print("testing sample fixure")
	print(samplefixure)

def test_samplefixture1(samplefixure):
	print("testing sample fixure1")
	print(samplefixure)